from rest_framework import serializers
from ..models.rental_form import RentalForm
from ..models.return_form import ReturnForm
from ..models.car import Car
from ..serializers.car_serializer import CarSerializer, SmallCarSerializer

class RentalFormSerializer(serializers.ModelSerializer):
    car = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all())

    class Meta:
        model = RentalForm
        fields = '__all__'


class ReturnFormSerializer(serializers.ModelSerializer):
    car = CarSerializer()

    class Meta:
        model = ReturnForm
        fields = '__all__'
