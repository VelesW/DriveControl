from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..services.rental_service import RentalFormService
from ..repositories.rental_repository import RentalFormRepository
from ..models.rental_form import RentalForm
from ..serializers.rental_form_serializer import RentalFormSerializer

rental_form_repository = RentalFormRepository(RentalForm)
rental_form_service = RentalFormService(rental_form_repository)

class RentalFormListCreateView(APIView):
    def get(self, request):
        rental_forms = rental_form_service.list_rental_forms()
        serializer = RentalFormSerializer(rental_forms, many=True)  # many=True because it's a list of rental forms
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            rental_form = rental_form_service.create_rental_form(request.data)
            # Serialize the created rental form
            serializer = RentalFormSerializer(rental_form)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class RentalFormDetailView(APIView):
    def get(self, request, rental_id):
        rental_form = rental_form_service.get_rental_form_by_id(rental_id)
        if rental_form:
            return Response(rental_form, status=status.HTTP_200_OK)
        return Response({"error": "RentalForm not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, rental_id):
        try:
            rental_form = rental_form_service.update_rental_form(rental_id, request.data)
            return Response(rental_form, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, rental_id):
        success = rental_form_service.delete_rental_form(rental_id)
        if success:
            return Response({"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "RentalForm not found"}, status=status.HTTP_404_NOT_FOUND)
