from email.policy import default
from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):

    email=models.EmailField(unique=True)


    USERNAME_FIELD ="email"
    REQUIRED_FIELDS =("username",)

    def __str__(self):
        return self.username

f='''
- Name
- E-mail
- Contact number
- Address
- Profile Picture
'''


class UserRegistration(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.EmailField( max_length=254)
    Contactnumber=models.CharField(max_length=10)
    Address=models.CharField(max_length=10)
    ProfilePicture=models.ImageField(default="default.png",blank=True,upload_to="images/")