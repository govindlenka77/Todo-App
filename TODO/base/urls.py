from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('update/<int:pk>',views.update,name='update'),
    path('delete/<int:pk>',views.delete,name="delete"),
    path('start/',views.start),
]