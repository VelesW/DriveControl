from ..serializers.form_serializers import SendRentalFormSerializer, GetRentalFormSerializer
from ..utils.price_calculator import calculate_price

class RentalFormService:
    def __init__(self, repository):
        self.repository = repository

    def create_rental_form(self, data):
        data['price'] = calculate_price(data['date_from'], data['date_to'], data['additional_options'], data['car'])
        serializer = SendRentalFormSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            return self.repository.create(serializer.validated_data)

    def get_rental_form_by_id(self, pk):
        rental_form = self.repository.get_by_id(pk)
        if rental_form:
            return GetRentalFormSerializer(rental_form).data
        return None

    def update_rental_form(self, pk, data):
        rental_form = self.repository.get_by_id(pk)
        if not rental_form:
            raise ValueError(f"RentalForm with ID {pk} does not exist.") 
        
        data['price'] = calculate_price(data['date_from'], data['date_to'], data['additional_options'], data['car'])

        serializer = SendRentalFormSerializer(rental_form, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            return self.repository.update(pk, serializer.validated_data)

    def delete_rental_form(self, pk):
        print(pk)
        return self.repository.delete(pk)

    def list_rental_forms(self):
        rental_forms = self.repository.list_all()
        return GetRentalFormSerializer(rental_forms, many=True).data
