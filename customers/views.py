from django.views.generic import ListView, DetailView
from .models import Customer

class CustomerListView(ListView):
    model = Customer
    template_name = 'customers/customer_list.html'

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customers/customer_detail.html'