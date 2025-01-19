# backend/api/controllers/car_controller.py

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from ..models.car import Car
from ..serializers.car_serializer import CarSerializer
from django.shortcuts import get_object_or_404
from ..services.car_service import CarService
from ..repositories.car_repository import CarRepository
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt


car_repository = CarRepository(Car)
car_service = CarService(car_repository)

class CarViewSet(viewsets.ViewSet):

    def list(self, request):
        cars = car_service.list_cars()
        return Response(cars)

    def create(self, request):
        car = car_service.create_car(request.data)
        if car:
            return Response(CarSerializer(car).data, status=status.HTTP_201_CREATED)
        return Response({"error": "Failed to create car"}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        car = car_service.get_car_by_id(pk)
        if car:
            return Response(car)
        return Response({"error": "Car not found"}, status=status.HTTP_404_NOT_FOUND)

    @csrf_exempt
    def update(self, request, pk=None):
        car = car_service.update_car(pk, request.data)
        if car:
            return Response(CarSerializer(car).data)
        return Response({"error": "Failed to update car"}, status=status.HTTP_400_BAD_REQUEST)
    
    @csrf_exempt
    def remove(self, request, pk=None):
        success = car_service.delete_car(pk)
        if success:
            return Response({"message": "Car deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Car not found"}, status=status.HTTP_404_NOT_FOUND)