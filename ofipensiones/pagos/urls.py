from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.pagos_view, name='pagos_view')
]
