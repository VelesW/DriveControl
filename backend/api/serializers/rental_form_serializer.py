from rest_framework import serializers
from ..models.rental_form import RentalForm

class RentalFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentalForm
        fields = '__all__'
