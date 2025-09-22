# customers/models.py
from django.db import models

class Customer(models.Model):
    customer_id = models.CharField(primary_key=True, max_length=25)
    customer_name = models.CharField(max_length=25, null=True, blank=True)
    gender = models.CharField(max_length=15, null=True, blank=True)
    job_title = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email_address = models.EmailField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=25, null=True, blank=True)
    country = models.CharField(max_length=40, null=True, blank=True)
    state = models.CharField(max_length=40, null=True, blank=True)
    customer_address = models.CharField(max_length=50, null=True, blank=True)
    postal_code = models.IntegerField(null=True, blank=True)
    credit_card_type = models.CharField(max_length=40, null=True, blank=True)
    credit_card_number = models.BigIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'Customer'

    def __str__(self):
        return self.customer_name