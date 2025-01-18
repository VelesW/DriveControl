from django.contrib import admin
from .models.system_user import SystemUser
from .models.rental_form import RentalForm

# Register your models here.
admin.site.register(RentalForm)
admin.site.register(SystemUser)
