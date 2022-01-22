
from django.contrib.auth.forms import UserCreationForm as ucf,AuthenticationForm

from django.contrib.auth import get_user_model

from .models import CustomUser,UserRegistration


from django.shortcuts import redirect, render
from django.http import HttpResponse, response
from django.contrib.auth import login,logout
from .forms import UserRegistrationForm
from .models import UserRegistration

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