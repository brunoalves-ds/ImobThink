from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.listarcliente),
    path('visualizar/<int:id>', views.visualizarcliente),
    path('novocliente/', views.novocliente),
    path('editarcliente/<int:id>', views.editarcliente),
    path('excluircliente/<int:id>', views.excluircliente),
    path('visualizarusuario/<str:nome>', views.visualizarusuario),
    path('visualizarimovel/<str:nome>', views.visualizarimovel),
]