from django.urls import path
from .views import CustomerListView, CustomerDetailView

urlpatterns = [
    path('', CustomerListView.as_view(), name='customer-list'),
    path('<str:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
]