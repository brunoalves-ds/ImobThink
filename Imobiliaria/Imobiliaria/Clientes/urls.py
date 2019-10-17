from django.urls import path

from . import views

urlpatterns = [
    path('helloworld/', views.helloWorld),
    path('', views.clienteList, name='task-list'),
    path('task/<int:id>', views.clienteView, name="task-view"),
    path('newtask/', views.newCliente, name="new-task"),
    path('edit/<int:id>', views.editCliente, name="edit-task"),
    path('delete/<int:id>', views.deleteCliente, name="delete-task"),

]