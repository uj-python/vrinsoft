
from django.contrib.auth.forms import UserCreationForm as ucf,AuthenticationForm

from django.contrib.auth import get_user_model

from .models import CustomUser,UserRegistration


from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse, response
from django.contrib.auth import login,logout
from .forms import UserRegistrationForm

from .serializers import UserSerializers,RegisteredSerializres


from rest_framework.views import APIView

from accounts import serializers

from rest_framework.response import Response

def register(request):
    msg=""
    if request.method=="POST":
        print(request.POST)
        form=UserRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('info')
        else:
            msg="some error occured"
    form=UserRegistrationForm
    return render(request,'register.html',{'form':form,'msg':msg})


def info(request):
    users = UserRegistration.objects.all()
    print(users)
    return render(request,'info.html',{'users':users})

def DeleteUser(request,name):
    user_obj=UserRegistration.objects.get(Name=name)
    user_obj.delete()
   
    return redirect('info')


class Usersapi(APIView):
    def get(self,request):
        users = CustomUser.objects.all()
        if users:
            serializer=UserSerializers(users,many=True)
            return Response(serializer.data)
        else:
            msg={'msg':'NO users yet'}
            return Response(msg)
    def post(self,request):
        serializer=UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            msg={'msg':'NO users yet'}
            return Response(msg)

    def put(self,request):
        print("------here---",request.data['id'])
        user=CustomUser.objects.get(id=request.data['id'])
        if user:
            serializer=UserSerializers(instance=user,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                msg={'msg':'NO users yet'}
                return Response(msg)

        else:
            msg={'msg':'NO users found'}
            return Response(msg)

    def delete(self,request,ipname):
        user=CustomUser.objects.get(name=ipname)
        if user:
            user.delete()
            msg={'msg':'User deleted succesfully'}
            return Response(msg)
        else:
            msg={'msg':'NO users found'}
            return Response(msg)




class RegisteredUser(APIView):
    def get(self,request):
        users = UserRegistration.objects.filter(Name='prajwal')
        if users:
            serializer=RegisteredSerializres(users,many=True)
            print("----------------------------serializer is----------",serializer)
            return Response(serializer.data)
        else:
            send={'msg':'NO users yet'}
            return Response(send)
