from django.urls import path
from app3 import views
app_name="app3"

urlpatterns=[
    
    path("<data>/",views.carry_data,name="carry_data"),
    path("fact/<num>/",views.facto,name="facto"),
    path("add/<num1>/<num2>",views.add,name="add"),



]