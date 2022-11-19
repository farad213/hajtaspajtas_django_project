from django.shortcuts import render, redirect
from .forms import CompanyForm, PrivatePersonForm, CustomUserForm
from .models import CustomUser


def register(request):
    context = {}
    return render(request, "accounts/register.html", context)


def register_company(request):
    user_creation_form = CustomUserForm(prefix="user_creation_form")
    company_form = CompanyForm(prefix="company_form")

    if request.method == "POST":
        user_creation_form = CustomUserForm(request.POST, prefix="user_creation_form")
        company_form = CompanyForm(request.POST, prefix="company_form")
        if user_creation_form.is_valid() and company_form.is_valid():
            user_creation_form.save()
            filled_company_form = company_form.save(commit=False)
            user = CustomUser.objects.get(username=request.POST["user_creation_form-username"])
            filled_company_form.is_company = user
            filled_company_form.save()

            return redirect("home")

    context = {"user_creation_form": user_creation_form, "company_form": company_form}
    return render(request, "accounts/register_company.html", context)


def register_private_person(request):
    user_creation_form = CustomUserForm(prefix="user_creation_form")
    private_person_form = PrivatePersonForm(prefix="company_form")

    if request.method == "POST":
        user_creation_form = CustomUserForm(request.POST, prefix="user_creation_form")
        private_person_form = PrivatePersonForm(request.POST, prefix="company_form")
        if user_creation_form.is_valid() and private_person_form.is_valid():
            user_creation_form.save()
            filled_private_person_form = private_person_form.save(commit=False)
            user = CustomUser.objects.get(username=request.POST["user_creation_form-username"])
            filled_private_person_form.is_private_person = user
            filled_private_person_form.save()

            return redirect("home")

    context = {"user_creation_form": user_creation_form, "private_person_form": private_person_form}
    return render(request, "accounts/register_private_person.html", context)
