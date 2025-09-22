from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet
from customers.views import CustomerViewSet
from shippers.views import ShipperViewSet
from orders.views import OrderViewSet

router = DefaultRouter()

router.register(r'products', ProductViewSet, basename='product')
router.register(r'customers', CustomerViewSet, basename='customer')
router.register(r'shippers', ShipperViewSet, basename='shipper')
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = router.urls