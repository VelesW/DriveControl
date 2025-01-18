from ..serializers.car_serializer import CarSerializer

class CarService:
    def __init__(self, repository):
        self.repository = repository

    def create_car(self, data):
        serializer = CarSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            return self.repository.create(serializer.validated_data)

    def get_car_by_id(self, car_id):
        car = self.repository.get_by_id(car_id)
        if car:
            return CarSerializer(car).data
        return None

    def update_car(self, car_id, data):
        car = self.repository.get_by_id(car_id)
        if not car:
            raise ValueError(f"Car with ID {car_id} does not exist.")

        serializer = CarSerializer(car, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            return self.repository.update(car_id, serializer.validated_data)

    def delete_car(self, car_id):
        return self.repository.delete(car_id)

    def list_cars(self):
        cars = self.repository.list_all()
        return CarSerializer(cars, many=True).data