from rest_framework.response import Response
from rest_framework import status
from ..services.return_service import ReturnFormService
from ..repositories.return_repository import ReturnFormRepository
from ..models.return_form import ReturnForm
from ..serializers.form_serializers import ReturnFormSerializer
from rest_framework.decorators import api_view

return_form_repository = ReturnFormRepository(ReturnForm)
return_form_service = ReturnFormService(return_form_repository)

@api_view(['GET'])
def get_return_forms(self):
    rental_forms = return_form_service.list_rental_forms()
    serializer = ReturnFormSerializer(rental_forms, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_return_form(request):
    serializer = ReturnFormSerializer(data=request.data)
    if serializer.is_valid():
        return_form_service.create_rental_form(request.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def edit_return_form(request, pk):
    try:
        rental_form = return_form_service.update_rental_form(pk, request.data)
        if rental_form:
            serializer = ReturnFormSerializer(rental_form)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "RentalForm not found"}, status=status.HTTP_404_NOT_FOUND)
    
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_return_form_detail(request, pk):
    rental_form = return_form_service.get_rental_form_by_id(pk)
    if rental_form:
        serializer = ReturnFormSerializer(rental_form)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({"error": "RentalForm not found"}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE', 'GET'])
def delete_return_form(request, pk):
    success = return_form_service.delete_rental_form(pk)
    if success:
        return Response({"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    return Response({"error": "RentalForm not found"}, status=status.HTTP_404_NOT_FOUND)
