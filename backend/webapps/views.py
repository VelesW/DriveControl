from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from api.serializers.authentication_serializers import RegisterSerializer, LoginSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

SystemUser = get_user_model()

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            serializer.data, 
            status=status.HTTP_201_CREATED
        )
    else:
        print(serializer.errors)
    return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_me(request):
    user = request.user
    serializer = LoginSerializer(user)
    return Response(serializer.data)

# @api_view(['POST'])
# def complete_rent_car_form(request):
