# orders/serializers.py
from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='order-detail')

    class Meta:
        model = Order
        fields = [
            'url', 'order_id', 'quantity', 'vehicle_price', 'order_date', 
            'ship_date', 'discount', 'ship_mode', 'shipping', 'customer_feedback', 
            'quarter_number', 'customer', 'shipper', 'product'
        ]