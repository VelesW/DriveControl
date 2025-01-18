# backend/api/controllers/registration_controller.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.authentication_serializers import RegisterSerializer

class RegistrationController(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MeController(APIView):
    def get(self, request):
        user = request.user
        user_data = {
            'username': user.username,
            'email': user.email,
        }
        return Response(user_data)
    