from django.db import models
class Shipper(models.Model):
    shipper_id = models.IntegerField(primary_key=True)
    shipper_name = models.CharField(max_length=50, null=True, blank=True)
    shipper_contact_details = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        db_table = 'Shippers'

    def __str__(self):
        return self.shipper_name