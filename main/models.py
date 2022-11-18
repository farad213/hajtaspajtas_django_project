from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    #general
    invoice_postal_code = models.CharField(max_length=10, verbose_name="Irányítószám")
    invoice_town = models.CharField(max_length=50, verbose_name="Város")
    invoice_address = models.CharField(max_length=150, verbose_name="Utca, házszám")
    invoice_country = models.CharField(max_length=50, verbose_name="Ország")

    #private person
    private_phone_number = models.CharField(max_length=50, verbose_name="Telefonszám")
    is_private_person = models.BooleanField()

    #company
    company_name = models.CharField(max_length=200, verbose_name="Cég neve")
    company_phone_number = models.CharField(max_length=50, verbose_name="Telefonszám")
    tax_number = models.CharField(max_length=50, verbose_name="Adószám")
    is_company = models.BooleanField()