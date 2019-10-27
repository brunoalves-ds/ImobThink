from django.urls import path
from . import views
urlpatterns = [
    path('', views.listarcliente),
    path('visualizar/<int:id>', views.visualizarcliente),
    path('novocliente/', views.novocliente),
    path('editarcliente/<int:id>', views.editarcliente),
    path('excluircliente/<int:id>', views.excluircliente),
]