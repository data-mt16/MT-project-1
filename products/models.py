# products/models.py
from django.db import models

class Product(models.Model):
    # SQL: product_id int NOT NULL (PRIMARY KEY)
    product_id = models.IntegerField(primary_key=True)

    # SQL: vehicle_maker varchar(60)
    vehicle_maker = models.CharField(max_length=60)

    # SQL: vehicle_model varchar(60)
    vehicle_model = models.CharField(max_length=60)

    # SQL: vehicle_color varchar(60)
    vehicle_color = models.CharField(max_length=60)

    # SQL: vehicle_model_year int
    vehicle_model_year = models.IntegerField()

    # SQL: vehicle_price decimal(14,8)
    vehicle_price = models.DecimalField(max_digits=14, decimal_places=8)
    
    class Meta:
        db_table = 'Products'

    def __str__(self):
        return f"{self.vehicle_model_year} {self.vehicle_maker} {self.vehicle_model}"