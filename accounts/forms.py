
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.contrib.auth.models import User

from .models import CustomUser,UserRegistration
from django import forms



class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model=CustomUser
        fields =("username","email")

class CustomUSerChangeForm(UserChangeForm):
    class Meta:
        model=CustomUser
        fields =("username","email")


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model=UserRegistration
        fields ="__all__"

