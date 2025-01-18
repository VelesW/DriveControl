from django.core.exceptions import ObjectDoesNotExist

class RentalFormRepository:
    def __init__(self, model):
        self.model = model

    def create(self, data):
        return self.model.objects.create(**data)

    def get_by_id(self, rental_id):
        try:
            return self.model.objects.get(id=rental_id)
        except ObjectDoesNotExist:
            return None

    def update(self, rental_id, data):
        rental_form = self.get_by_id(rental_id)
        if rental_form:
            for field, value in data.items():
                setattr(rental_form, field, value)
            rental_form.full_clean()
            rental_form.save()
            return rental_form
        return None

    def delete(self, rental_id):
        rental_form = self.get_by_id(rental_id)
        if rental_form:
            rental_form.delete()
            return True
        return False

    def list_all(self):
        return self.model.objects.all()
