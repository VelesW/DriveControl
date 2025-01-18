from rest_framework import serializers
from ..models.system_user import SystemUser

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = SystemUser
        fields = ['id','username','email','password']

    def create(self, validated_data):
        print("Validated data:", validated_data)

        user = SystemUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemUser
        fields = ['id','username','password']
