from django.db import models


class RentalForm(models.Model):
    renter_name = models.CharField(max_length=255)
    renter_surname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    # car_photo = models.ImageField(upload_to='car_photos/')
    # equipment_photo = models.ImageField(upload_to='equipment_photos/')
    fuel_level = models.DecimalField(max_digits=5, decimal_places=2)
    signature = models.TextField()

    def __str__(self):
        return f"RentalForm for {self.renter_name} {self.renter_surname}"
