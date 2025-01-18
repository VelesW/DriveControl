from ..models.rental_form import RentalForm

class RentalRepository:
    def save_form(self, form_data):
        rental_form = RentalForm.objects.create(**form_data)
        return rental_form

    def validate_signature(self, signature):
        # Placeholder logic for signature validation
        return True
