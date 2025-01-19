from ..serializers.form_serializers import SendReturnFormSerializer, GetReturnFormSerializer

class ReturnFormService:
    def __init__(self, repository):
        self.repository = repository

    def create_rental_form(self, data):
        serializer = SendReturnFormSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            return self.repository.create(serializer.validated_data)

    def get_rental_form_by_id(self, pk):
        rental_form = self.repository.get_by_id(pk)
        if rental_form:
            return GetReturnFormSerializer(rental_form).data
        return None

    def update_rental_form(self, pk, data):
        rental_form = self.repository.get_by_id(pk)
        if not rental_form:
            raise ValueError(f"RentalForm with ID {pk} does not exist.")

        serializer = SendReturnFormSerializer(rental_form, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            return self.repository.update(pk, serializer.validated_data)

    def delete_rental_form(self, pk):
        print(pk)
        return self.repository.delete(pk)

    def list_rental_forms(self):
        rental_forms = self.repository.list_all()
        return GetReturnFormSerializer(rental_forms, many=True).data
