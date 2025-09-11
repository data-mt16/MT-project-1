from django.urls import path
from .views import ShipperListView, ShipperDetailView

urlpatterns = [
    path('', ShipperListView.as_view(), name='shipper-list'),
    path('<int:pk>/', ShipperDetailView.as_view(), name='shipper-detail'),
]