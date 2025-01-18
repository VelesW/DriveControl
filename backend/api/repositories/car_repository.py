from django.core.exceptions import ObjectDoesNotExist
from ..models.car import Car

class CarRepository:
    def __init__(self, model):
        self.model = model

    def create(self, data):
        return self.model.objects.create(**data)

    def get_by_id(self, car_id):
        try:
            return self.model.objects.get(id=car_id)
        except ObjectDoesNotExist:
            return None

    def update(self, car_id, data):
        car = self.get_by_id(car_id)
        if car:
            for field, value in data.items():
                setattr(car, field, value)
            car.full_clean()
            car.save()
            return car
        return None

    def delete(self, car_id):
        car = self.get_by_id(car_id)
        if car:
            car.delete()
            return True
        return False

    def list_all(self):
        return self.model.objects.all()