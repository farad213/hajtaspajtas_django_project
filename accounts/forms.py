from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, PrivatePerson, Company
from django import forms


class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "password1", "password2"]


class PrivatePersonForm(forms.ModelForm):
    class Meta:
        model = PrivatePerson
        fields = ["last_name", "first_name", "phone_number", "invoice_postal_code", "invoice_town", "invoice_address",
                  "invoice_country"]


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ["company_name", "company_phone_number", "tax_number", "invoice_postal_code",
                  "invoice_town", "invoice_address", "invoice_country"]
