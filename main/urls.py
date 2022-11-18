from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('prices/', views.prices, name="prices"),
    path('online_order/', views.online_order, name="online_order"),
    path('contact/', views.contact, name="contact"),
    path('about_us/', views.about_us, name="about us"),
    path('budapest/', views.budapest, name="budapest"),
    path('videk/', views.videk, name="videk"),
    path('kulfold/', views.kulfold, name="kulfold"),
    path('register/', views.register, name="register"),
    path('register_company/', views.register_company, name="register_company"),
    path('register_private_person/', views.register_private_person, name="register_private_person"),
]