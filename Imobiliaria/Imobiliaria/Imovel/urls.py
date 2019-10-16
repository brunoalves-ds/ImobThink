from django.urls import path

from . import views

urlpatterns = [
    path('', views.imovelList, name='imovel-list'),
    path('imovel/<int:id>',views.imovelView, name='imovel-view'),
    path('editarImovel/<int:id>',views.editarImovel, name='editar-imovel'),
    path('cadastrarImovel/',views.cadastrarImovel, name='cadastrar-imovel'),
]