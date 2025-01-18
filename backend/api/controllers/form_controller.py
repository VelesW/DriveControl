from rest_framework.response import Response
from rest_framework import status
from ..services.rental_service import RentalFormService
from ..repositories.rental_repository import RentalFormRepository
from ..models.rental_form import RentalForm
from ..serializers.rental_form_serializer import RentalFormSerializer
from rest_framework.decorators import api_view

rental_form_repository = RentalFormRepository(RentalForm)
rental_form_service = RentalFormService(rental_form_repository)

@api_view(['GET'])
def get_rental_forms(self):
    rental_forms = rental_form_service.list_rental_forms()
    serializer = RentalFormSerializer(rental_forms, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_rental_form(request):
    serializer = RentalFormSerializer(data=request.data)
    if serializer.is_valid():
        rental_form_service.create_rental_form(request.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def edit_rental_form(request, rental_id):
    try:
        rental_form = rental_form_service.update_rental_form(rental_id, request.data)
        if rental_form:
            serializer = RentalFormSerializer(rental_form)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "RentalForm not found"}, status=status.HTTP_404_NOT_FOUND)
    
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_form_detail(request, rental_id):
    rental_form = rental_form_service.get_rental_form_by_id(rental_id)
    if rental_form:
        serializer = RentalFormSerializer(rental_form)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({"error": "RentalForm not found"}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE', 'GET'])
def delete_rental_form(request, rental_id):
    success = rental_form_service.delete_rental_form(rental_id)
    if success:
        return Response({"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    return Response({"error": "RentalForm not found"}, status=status.HTTP_404_NOT_FOUND)
