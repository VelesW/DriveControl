from django.urls import path
from webapps.views import (register, get_me)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.controllers.rental_form_controller import get_rental_forms, add_rental_form, edit_rental_form, get_form_detail, delete_rental_form
from api.controllers.return_form_controller import get_return_forms, add_return_form, edit_return_form, get_return_form_detail, delete_return_form

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', register, name='register'),
    path('me/', get_me, name='get_me'),
    path('rental-forms/', get_rental_forms, name='rental_form_list'),
    path('rental-form/add/', add_rental_form, name='rental_form_create'),
    path('rental-form/edit/<int:pk>/', edit_rental_form, name='rental_form_edit'),
    path('rental-form/delete/<int:pk>/', delete_rental_form, name='rental_form_delete'),
    path('rental-form/get/<int:pk>/', get_form_detail, name='rental_form_get'),
    path('return-forms/', get_return_forms, name='return_form_list'),
    path('return-form/add/', add_return_form, name='return_form_create'),
    path('return-form/edit/<int:pk>/', edit_return_form, name='return_form_edit'),
    path('return-form/delete/<int:pk>/', delete_return_form, name='return_form_delete'),
    path('return-form/get/<int:pk>/', get_return_form_detail, name='return_form_get'),
]