from django.contrib import admin
from django.urls import path, include
from .webapps.views import (
    business_user_list, business_user_delete,
    register, get_concrete_business_user, business_user_update,
    get_me
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.controllers.form_controller import FormController
from api.services.rental_service import RentalService
from api.repositories.rental_repository import RentalRepository
from api.utils.signature_validator import SignatureValidator

rental_repository = RentalRepository()
signature_validator = SignatureValidator()
rental_service = RentalService(rental_repository, signature_validator)
form_controller = FormController.as_view(rental_service=rental_service)

urlpatterns = [
    path('users/', business_user_list, name='business_user_list'),
    path('users/<int:pk>/delete/', business_user_delete, name='user_delete'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', register, name='register'),
    path('users/<int:pk>/update/', business_user_update, name='user_update'),
    path('users/<int:pk>/', get_concrete_business_user, name='user_get_concrete'),
    path('me/', get_me, name='get_me'),
    path('submit-form/', form_controller, name='submit-form'),
]