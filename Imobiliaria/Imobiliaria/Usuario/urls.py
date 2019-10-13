from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.listarusuario),
    path('novousuario/', views.novousuario),
    path('editarusuario/<int:id>', views.editarusuario),
    path('excluirusuario/<int:id>', views.excluirusuario),

]
