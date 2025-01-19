from django.db import models
from .car import Car

class ReturnForm(models.Model):
    renter_name = models.CharField(max_length=255, blank=False)
    renter_surname = models.CharField(max_length=255, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    fuel_level = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()
    additional_options = models.TextField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    signature = models.TextField(blank=False)

    def __str__(self):
        return f"RentalForm for {self.renter_name} {self.renter_surname}"
