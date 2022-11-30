from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, PrivatePerson, Company
from django import forms


class CustomUserForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Jelszó'}),
        error_messages={'required': 'Hiányzó "Jelszó" mező', 'password_mismatch': "A kettő jelszó nem egyezik meg"})

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Jelszó újra'}),
        error_messages={'required': 'Hiányzó "Jelszó újra" mező',
                        'password_mismatch': "A kettő jelszó nem egyezik meg"})

    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Felhasználónév"}),
        error_messages={'required': 'Hiányzó "Felhasználónév" mező'})

    class Meta:
        model = CustomUser
        fields = ["username", "password1", "password2"]


class PrivatePersonForm(forms.ModelForm):
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Keresztnév"}),
        error_messages={'required': 'Hiányzó "Keresztnév" mező'})

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Vezetéknév"}),
        error_messages={'required': 'Hiányzó "Vezetéknév" mező'})

    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Telefonszám"}),
        error_messages={'required': 'Hiányzó "Telefonszám" mező'})

    invoice_postal_code = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Irányítószám"}),
        error_messages={'required': 'Hiányzó "Irányítószám" mező'})

    invoice_town = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Város"}),
        error_messages={'required': 'Hiányzó "Város" mező'})

    invoice_address = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Utca, házszám, emelet..."}),
        error_messages={'required': 'Hiányzó "Utca, házszám, emelet..." mező'})

    invoice_country = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Ország"}),
        error_messages={'required': 'Hiányzó "Ország" mező'})

    class Meta:
        model = PrivatePerson
        fields = ["last_name", "first_name", "phone_number", "invoice_postal_code", "invoice_town", "invoice_address",
                  "invoice_country"]


class CompanyForm(forms.ModelForm):
    company_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Cég neve"}),
        error_messages={'required': 'Hiányzó "Cég neve" mező'})

    company_phone_number = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Központi telefonszám"}),
        error_messages={'required': 'Hiányzó "Központi telefonszám" mező'})

    tax_number = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Adószám"}),
        error_messages={'required': 'Hiányzó "Adószám" mező'})

    invoice_postal_code = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Irányítószám"}),
        error_messages={'required': 'Hiányzó "Irányítószám" mező'})

    invoice_town = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Város"}),
        error_messages={'required': 'Hiányzó "Város" mező'})

    invoice_address = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Utca, házszám, emelet..."}),
        error_messages={'required': 'Hiányzó "Utca, házszám, emelet..." mező'})

    invoice_country = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Ország"}),
        error_messages={'required': 'Hiányzó "Ország" mező'})

    class Meta:
        model = Company
        fields = ["company_name", "company_phone_number", "tax_number", "invoice_postal_code",
                  "invoice_town", "invoice_address", "invoice_country"]
