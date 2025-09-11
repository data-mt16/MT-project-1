from django.views.generic import ListView, DetailView
from .models import Shipper

class ShipperListView(ListView):
    model = Shipper
    template_name = 'shippers/shipper_list.html'
    context_object_name = 'shippers' # Optional: for a friendlier name in template

class ShipperDetailView(DetailView):
    model = Shipper
    template_name = 'shippers/shipper_detail.html'
    context_object_name = 'shipper'


from rest_framework import viewsets
from .models import Shipper
from .serializers import ShipperSerializer


class ShipperViewSet(viewsets.ModelViewSet):
    queryset = Shipper.objects.all()
    serializer_class = ShipperSerializer