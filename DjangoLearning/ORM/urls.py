from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import views
from .views import RegisterUser

urlpatterns = [
    path('' , views.home, name='home'),
    path('register',  RegisterUser.as_view(), name='registration'),
    #path('<int:pk>', BoockDeatail.as_view() ,name='show_boock')
    path('boock/<slug:boock_name>' , views.detail_boock, name='boock'),
    path('cat/<int:cat_id', views.show_cat, name='show_cat')

]