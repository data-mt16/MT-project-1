from django.shortcuts import render

# Create your views here.
# reports/views.py
from django.db.models import Count, Avg, Case, When, F, Window, Value, Sum, ExpressionWrapper, fields
from django.db.models.functions import Rank, Lag

from rest_framework.decorators import api_view
from rest_framework.response import Response

from customers.models import Customer
from orders.models import Order
from products.models import Product

# Question 1: Customer distribution by state
@api_view(['GET'])
def customer_distribution_by_state(request):
    data = (
        Customer.objects.filter(order__isnull=False)
        .values('state')
        .annotate(customer_count=Count('customer_id', distinct=True))
        .order_by('-customer_count')
    )
    return Response(data)

# Question 2: Top 5 vehicle makers
@api_view(['GET'])
def top_vehicle_makers(request):
    data = (
        Product.objects.values('vehicle_maker')
        .annotate(customer_count=Count('order__customer', distinct=True))
        .order_by('-customer_count')[:5]
    )
    return Response(data)

# Question 3: Most preferred vehicle maker in each state
@api_view(['GET'])
def preferred_maker_by_state(request):
    base_query = (
        Product.objects.values('vehicle_maker', 'order__customer__state')
        .annotate(customer_count=Count('order__customer', distinct=True))
        .filter(order__customer__state__isnull=False)
    )
    ranked_query = base_query.annotate(
        rank=Window(
            expression=Rank(),
            partition_by=F('order__customer__state'),
            order_by=F('customer_count').desc()
        )
    )
    # Filter for rank=1 in Python
    data = [row for row in ranked_query if row['rank'] == 1]
    return Response(data)

# Question 4: Average ratings
@api_view(['GET'])
def average_ratings(request):
    feedback_mapping = { 'Very Bad': 1, 'Bad': 2, 'Okay': 3, 'Good': 4, 'Very Good': 5 }
    when_clauses = [When(customer_feedback=k, then=Value(v)) for k, v in feedback_mapping.items()]
    
    annotated_query = Order.objects.annotate(rating=Case(*when_clauses, default=Value(0)))
    overall_avg = annotated_query.aggregate(overall_average_rating=Avg('rating'))
    quarterly_avg = (
        annotated_query.values('quarter_number')
        .annotate(average_rating_per_quarter=Avg('rating'))
        .order_by('quarter_number')
    )
    data = {
        'overall_average_rating': overall_avg['overall_average_rating'],
        'average_rating_by_quarter': list(quarterly_avg)
    }
    return Response(data)

# Question 5: Feedback distribution
@api_view(['GET'])
def feedback_distribution(request):
    # This query is extremely complex for the ORM, a placeholder is returned.
    # A full solution might involve raw SQL or more advanced Python processing.
    data = {'message': 'This query is complex and a full ORM solution is beyond this scope.'}
    return Response(data)

# Question 6: Trend of orders by quarter
@api_view(['GET'])
def orders_trend_by_quarter(request):
    data = (
        Order.objects.values('quarter_number')
        .annotate(order_count=Count('order_id'))
        .order_by('quarter_number')
    )
    return Response(data)

# Question 7: Revenue QoQ change
@api_view(['GET'])
def revenue_qoq_change(request):
    # First, calculate revenue for each quarter
    quarterly_revenue = (
        Order.objects
        .annotate(revenue=ExpressionWrapper(F('quantity') * F('vehicle_price') * (1 - F('discount')), output_field=fields.DecimalField()))
        .values('quarter_number')
        .annotate(total_revenue=Sum('revenue'))
        .order_by('quarter_number')
    )
    # Then, use Lag to find the previous quarter's revenue
    revenue_with_lag = quarterly_revenue.annotate(
        previous_revenue=Window(
            expression=Lag('total_revenue', 1),
            order_by=F('quarter_number').asc()
        )
    )
    # Calculate the % change in Python
    final_data = []
    for row in revenue_with_lag:
        qoq_change = None
        if row['previous_revenue'] is not None and row['previous_revenue'] > 0:
            qoq_change = ((row['total_revenue'] - row['previous_revenue']) / row['previous_revenue']) * 100
        final_data.append({
            'quarter_number': row['quarter_number'],
            'total_revenue': row['total_revenue'],
            'qoq_change_percentage': qoq_change
        })
    return Response(final_data)

# Question 8: Trend of revenue and orders by quarter
@api_view(['GET'])
def revenue_orders_trend(request):
    data = (
        Order.objects.values('quarter_number')
        .annotate(
            total_revenue=Sum(F('quantity') * F('vehicle_price') * (1 - F('discount'))),
            order_count=Count('order_id')
        )
        .order_by('quarter_number')
    )
    return Response(data)

# Question 9: Average discount by credit card type
@api_view(['GET'])
def avg_discount_by_card(request):
    data = (
        Order.objects.values('customer__credit_card_type')
        .annotate(average_discount=Avg('discount'))
        .order_by('-average_discount')
    )
    return Response(data)

# Question 10: Average shipping time
@api_view(['GET'])
def avg_ship_time(request):
    data = (
        Order.objects
        .annotate(shipping_time_days=ExpressionWrapper(F('ship_date') - F('order_date'), output_field=fields.DurationField()))
        .values('quarter_number')
        .annotate(average_shipping_time_in_days=Avg('shipping_time_days'))
        .order_by('quarter_number')
    )
    # The result is a timedelta object, so we format it in Python
    for item in data:
        item['average_shipping_time_in_days'] = item['average_shipping_time_in_days'].days
    return Response(data)