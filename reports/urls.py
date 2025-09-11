from django.urls import path
from . import views

urlpatterns = [
    path('customer-distribution/', views.customer_distribution_by_state, name='report-customer-distribution'),
    path('top-vehicle-makers/', views.top_vehicle_makers, name='report-top-vehicle-makers'),
    path('preferred-maker-by-state/', views.preferred_maker_by_state, name='report-preferred-maker-by-state'),
    path('average-ratings/', views.average_ratings, name='report-average-ratings'),
    path('feedback-distribution/', views.feedback_distribution, name='report-feedback-distribution'),
    path('orders-trend-by-quarter/', views.orders_trend_by_quarter, name='report-orders-trend'),
    path('revenue-qoq-change/', views.revenue_qoq_change, name='report-revenue-qoq'),
    path('revenue-orders-trend/', views.revenue_orders_trend, name='report-revenue-orders-trend'),
    path('avg-discount-by-card/', views.avg_discount_by_card, name='report-avg-discount-by-card'),
    path('avg-ship-time/', views.avg_ship_time, name='report-avg-ship-time'),
]