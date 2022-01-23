from django import urls
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .import views

from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
 url(r'^register$',views.register,name='register'),
 url(r'^info$',views.info,name='info'),
  path('delete/<str:name>',views.DeleteUser,name="delete"),
  url(r'^userapi$',views.Usersapi.as_view(),name='userapi'),
  url(r'^registeredapi$',views.RegisteredUser.as_view(),name='registeredapi')
]


urlpatterns+=staticfiles_urlpatterns()

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

