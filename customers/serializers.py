# customers/serializers.py
from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='customer-detail')

    class Meta:
        model = Customer
        fields = [
            'url', 'customer_id', 'customer_name', 'gender', 'job_title', 
            'phone_number', 'email_address', 'city', 'country', 'state', 
            'customer_address', 'postal_code', 'credit_card_type', 'credit_card_number'
        ]