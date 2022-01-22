from corsheaders import django


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUSerChangeForm,CustomUserCreationForm

from .models import CustomUser,UserRegistration

class CustomUserAdmin(UserAdmin):
    add_form=CustomUserCreationForm
    form = CustomUSerChangeForm
    model=CustomUser


admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(UserRegistration)