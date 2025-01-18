from django.contrib import admin
from .models import BusinessUser, SystemUser
from .modelss.rental_form import RentalForm

# Register your models here.
admin.site.register(RentalForm)
admin.site.register(SystemUser)
admin.site.register(BusinessUser)
