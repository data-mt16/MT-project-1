from django.views.generic import ListView, DetailView
from .models import Customer

class CustomerListView(ListView):
    model = Customer
    template_name = 'customers/customer_list.html'

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customers/customer_detail.html'



from rest_framework import viewsets
from .models import Customer
from .serializers import CustomerSerializer

# Your old webpage views can stay, this is for the API
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer