from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..services.rental_service import RentalService


class FormController(APIView):
    def __init__(self, rental_service: RentalService, **kwargs):
        super().__init__(**kwargs)
        self.rental_service = rental_service

    def post(self, request):
        form_data = request.data

        try:
            rental_form = self.rental_service.handle_form_submission(form_data)
            return Response(
                {"message": "Form submitted successfully", "form_id": rental_form.id},
                status=status.HTTP_201_CREATED,
            )
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
