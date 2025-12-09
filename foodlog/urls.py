from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
    path('', views.food_list_create, name='list'),
    path('delete/<int:pk>/', views.food_delete, name='delete'),
]
