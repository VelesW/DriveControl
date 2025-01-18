from django.urls import path
from webapps.views import (register, get_me)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.utils.signature_validator import SignatureValidator
from api.controllers.form_controller import RentalFormListCreateView, RentalFormDetailView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', register, name='register'),
    path('me/', get_me, name='get_me'),
    path('rental-forms/', RentalFormListCreateView.as_view(), name='rental_form_list_create'),
    path('rental-forms/<int:rental_id>/', RentalFormDetailView.as_view(), name='rental_form_detail'),
]