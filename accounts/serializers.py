from django.contrib.auth.models import User
from rest_framework import  serializers
from .models import CustomUser,UserRegistration



class UserSerializers(serializers.ModelSerializer):
 
    class Meta:
      
        model = CustomUser
        
        fields = ('id','username', 'email')


class RegisteredSerializres(serializers.ModelSerializer):
    class Meta:
        model =UserRegistration
        fields='__all__'