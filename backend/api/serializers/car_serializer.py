from rest_framework import serializers
from ..models.car import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class SmallCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id']
