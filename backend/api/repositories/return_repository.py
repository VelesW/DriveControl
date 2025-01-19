from django.core.exceptions import ObjectDoesNotExist

class ReturnFormRepository:
    def __init__(self, model):
        self.model = model

    def create(self, data):
        return self.model.objects.create(**data)

    def get_by_id(self, pk):
        try:
            return self.model.objects.select_related('car').get(id=pk)
        except ObjectDoesNotExist:
            return None

    def update(self, pk, data):
        rental_form = self.get_by_id(pk)
        if rental_form:
            for field, value in data.items():
                setattr(rental_form, field, value)
            rental_form.full_clean()
            rental_form.save()
            return rental_form
        return None

    def delete(self, pk):
        rental_form = self.get_by_id(pk)
        if rental_form:
            rental_form.delete()
            return True
        return False

    def list_all(self):
        return self.model.objects.select_related('car').all()
