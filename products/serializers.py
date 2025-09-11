# products/serializers.py
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    # This new line adds a URL field to our API
    url = serializers.HyperlinkedIdentityField(view_name='product-detail')

    class Meta:
        model = Product
        # We now have to list all fields explicitly to include our new 'url' field
        fields = ['url', 'product_id', 'vehicle_maker', 'vehicle_model', 'vehicle_model_year', 'vehicle_price']