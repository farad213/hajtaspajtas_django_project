from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CompanyForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["company_name", "company_phone_number", "invoice_postal_code", "invoice_town", "invoice_address",
                  "invoice_country", "tax_number", "is_company", "is_private_person", "username"]


class PrivatePersonForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["private_phone_number", "first_name", "last_name", "invoice_postal_code", "invoice_town", "invoice_address",
                  "invoice_country", "is_company", "is_private_person", "username"]