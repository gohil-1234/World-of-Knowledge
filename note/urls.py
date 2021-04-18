from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('post-details/<str:id>/', views.detail),
    path('delete/<str:id>/', views.delete),
    path('upload/', views.upload),
]
