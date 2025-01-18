from django.urls import path
from webapps.views import (register, get_me)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.utils.signature_validator import SignatureValidator
from api.controllers.form_controller import get_rental_forms, add_rental_form, edit_rental_form, get_form_detail, delete_rental_form

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', register, name='register'),
    path('me/', get_me, name='get_me'),
    path('rental-forms/', get_rental_forms, name='rental_form_list'),
    path('rental-form/add/', add_rental_form, name='rental_form_create'),
    path('rental-form/edit/<int:rental_id>/', edit_rental_form, name='rental_form_edit'),
    path('rental-form/delete/<int:rental_id>/', delete_rental_form, name='rental_form_delete'),
    path('rental-form/get/<int:rental_id>/', get_form_detail, name='rental_form_get'),
]