from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # is_company = models.BooleanField()
    # is_private_person = models.BooleanField()
    pass

class PrivatePerson(models.Model):
    is_private_person = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=50, verbose_name="Telefonszám")
    invoice_postal_code = models.CharField(max_length=10, verbose_name="Irányítószám")
    invoice_town = models.CharField(max_length=50, verbose_name="Város")
    invoice_address = models.CharField(max_length=150, verbose_name="Utca, házszám")
    invoice_country = models.CharField(max_length=50, verbose_name="Ország")
    last_name = models.CharField(max_length=50, verbose_name="Vezetéknén")
    first_name = models.CharField(max_length=50, verbose_name="Keresztnév")

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

class Company(models.Model):
    is_company = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200, verbose_name="Cég neve")
    company_phone_number = models.CharField(max_length=50, verbose_name="Telefonszám")
    tax_number = models.CharField(max_length=50, verbose_name="Adószám")
    invoice_postal_code = models.CharField(max_length=10, verbose_name="Irányítószám")
    invoice_town = models.CharField(max_length=50, verbose_name="Város")
    invoice_address = models.CharField(max_length=150, verbose_name="Utca, házszám")
    invoice_country = models.CharField(max_length=50, verbose_name="Ország")

    def __str__(self):
        return self.company_name
