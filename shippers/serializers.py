# shippers/serializers.py
from rest_framework import serializers
from .models import Shipper

class ShipperSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='shipper-detail')

    class Meta:
        model = Shipper
        fields = ['url', 'shipper_id', 'shipper_name', 'shipper_contact_details']