from rest_framework import serializers
from ..models.rental_form import RentalForm
from ..models.return_form import ReturnForm
from ..models.car import Car
from ..serializers.car_serializer import CarSerializer, CarIDSerializer

class SendRentalFormSerializer(serializers.ModelSerializer):
    car = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all())

    class Meta:
        model = RentalForm
        fields = '__all__'

class GetRentalFormSerializer(serializers.ModelSerializer):
    car = CarIDSerializer()

    class Meta:
        model = RentalForm
        fields = '__all__'


class SendReturnFormSerializer(serializers.ModelSerializer):
    car = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all())

    class Meta:
        model = ReturnForm
        fields = '__all__'

class GetReturnFormSerializer(serializers.ModelSerializer):
    car = CarIDSerializer()

    class Meta:
        model = ReturnForm
        fields = '__all__'