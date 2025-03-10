from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiview),
    path('task_list/',views.task_list,name='task_list'),
    path('create/',views.create,name='create'),
    path('update/<int:pk>',views.update,name='update'),
    path('delete/<str:pk>',views.delete,name='delete'),
]