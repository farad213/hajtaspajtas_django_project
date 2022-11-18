from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('register_company/', views.register_company, name="register_company"),
    path('register_private_person/', views.register_private_person, name="register_private_person"),
]