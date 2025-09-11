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