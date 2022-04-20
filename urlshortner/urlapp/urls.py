from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.add, name='create'),
    path('<str:pk>', views.shorten, name='shorten'),
    path('user/', views.my_view, name='my_view')
]
