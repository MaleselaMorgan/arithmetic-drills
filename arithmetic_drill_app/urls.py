from django.urls import path
from . import views

urlpatterns = [
    path('', views.arithmetic_drill, name='arithmetic_drill'),
]
