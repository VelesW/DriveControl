from django.contrib import admin
from .models.system_user import SystemUser
from .models.rental_form import RentalForm
from .models.return_form import ReturnForm
from .models.car import Car

# Register your models here.
admin.site.register(RentalForm)
admin.site.register(SystemUser)
admin.site.register(ReturnForm)
admin.site.register(Car)

