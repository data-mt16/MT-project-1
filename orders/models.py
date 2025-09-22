# orders/models.py
from django.db import models

class Order(models.Model):
    order_id = models.CharField(primary_key=True, max_length=25)

    # --- Relationships (Foreign Keys) ---
    # This links to the Customer model in the 'customers' app.
    # on_delete=models.CASCADE means if a customer is deleted, their orders are also deleted.
    customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE, null=True)

    # This links to the Shipper model in the 'products' app.
    shipper = models.ForeignKey('shippers.Shipper', on_delete=models.CASCADE, null=True)

    # This links to the Product model in the 'products' app.
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, null=True)

    # --- Other Fields ---
    quantity = models.IntegerField(null=True, blank=True)
    vehicle_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    order_date = models.DateField(null=True, blank=True)
    ship_date = models.DateField(null=True, blank=True)
    discount = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    ship_mode = models.CharField(max_length=25, null=True, blank=True)
    shipping = models.CharField(max_length=30, null=True, blank=True)
    customer_feedback = models.CharField(max_length=20, null=True, blank=True)
    quarter_number = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'Order'

    def __str__(self):
        return self.order_id