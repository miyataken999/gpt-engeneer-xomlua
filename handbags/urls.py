from django.urls import path
from . import views

urlpatterns = [
    path('', views.handbag_list, name='handbag_list'),
    path('<int:pk>/', views.handbag_detail, name='handbag_detail'),
]