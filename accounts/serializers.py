from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from .models import CustomUser,UserRegistration



class UserSerializers(serializers.ModelSerializer):
    print("------here in the serializers class---------")
    class Meta:
        print("------inside the meta ---------")
        model = CustomUser
        fields = '__all__'
        # fields = ('username', 'email')


class RegisteredSerializres(serializers.ModelSerializer):
    class Meta:
        model =UserRegistration
        fields='__all__'