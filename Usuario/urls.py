from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.listarusuario),
    path('novousuario/', views.novousuario),
    path('editarusuario/<int:id>', views.editarusuario),
    path('excluirusuario/<int:id>', views.excluirusuario),
    path('inativado/', views.inativado),
    path('visualizar/<int:id>', views.visualizar),
    path('visualizarinativado/<int:id>', views.visualizarinativado),
]
