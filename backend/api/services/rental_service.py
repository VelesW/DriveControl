from ..serializers.rental_form_serializer import RentalFormSerializer

class RentalFormService:
    def __init__(self, repository):
        self.repository = repository

    def create_rental_form(self, data):
        serializer = RentalFormSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            return self.repository.create(serializer.validated_data)

    def get_rental_form_by_id(self, rental_id):
        rental_form = self.repository.get_by_id(rental_id)
        if rental_form:
            return RentalFormSerializer(rental_form).data
        return None

    def update_rental_form(self, rental_id, data):
        rental_form = self.repository.get_by_id(rental_id)
        if not rental_form:
            raise ValueError(f"RentalForm with ID {rental_id} does not exist.")

        serializer = RentalFormSerializer(rental_form, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            return self.repository.update(rental_id, serializer.validated_data)

    def delete_rental_form(self, rental_id):
        return self.repository.delete(rental_id)

    def list_rental_forms(self):
        rental_forms = self.repository.list_all()
        return RentalFormSerializer(rental_forms, many=True).data
