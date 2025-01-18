from django.db import models

class Car(models.Model):
    available = models.BooleanField()
    manufacturer = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    petrol_type = models.CharField(max_length=20, choices=[('petrol', 'Petrol'), ('diesel', 'Diesel'), ('electric', 'Electric')])
    drive_type = models.CharField(max_length=20, choices=[('fwd', 'FWD'), ('rwd', 'RWD'), ('awd', 'AWD')])
    segment = models.CharField(max_length=20, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('J', 'J'), ('M', 'M'), ('S', 'S')])
    horse_power = models.IntegerField()
    price_per_day = models.DecimalField(max_digits=8, decimal_places=2)

def __str__(self) -> str:
    return f"{self.year} {self.make} {self.model} - {self.segment}"