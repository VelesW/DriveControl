from django.urls import path
from ..webapps.views import (register, get_me)
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
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', register, name='register'),
    path('me/', get_me, name='get_me'),
    path('submit-form/', form_controller, name='submit-form'),
]