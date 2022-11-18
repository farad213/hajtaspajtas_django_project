from django.shortcuts import render
from .forms import CompanyForm, PrivatePersonForm



def register(request):
    context = {}
    return render(request, "accounts/register.html", context)


def register_company(request):
    form = CompanyForm(initial={'is_company': True, "is_private_person": False})

    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()

    context = {"form": form}
    return render(request, "accounts/register_company.html", context)


def register_private_person(request):
    form = PrivatePersonForm(initial={'is_company': False, "is_private_person": True})

    if request.method == "POST":
        form = PrivatePersonForm(request.POST)
        if form.is_valid():
            form.save()

    context = {"form": form}
    return render(request, "accounts/register_private_person.html", context)
