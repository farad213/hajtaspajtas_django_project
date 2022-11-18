from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import CompanyForm, PrivatePersonForm

def home(request):
    context = {}
    return render(request, "main/home.html", context)

def prices(request):
    context = {}
    return render(request, "main/prices.html", context)

def online_order(request):
    context = {}
    return render(request, "main/online_order.html", context)

def contact(request):
    context = {}
    return render(request, "main/conatct.html", context)

def about_us(request):
    context = {}
    return render(request, "main/about_us.html", context)

def budapest(request):
    context = {}
    return render(request, "main/budapest.html", context)

def videk(request):
    context = {}
    return render(request, "main/videk.html", context)

def kulfold(request):
    context = {}
    return render(request, "main/kulfold.html", context)

def register(request):
    context = {}
    return render(request, "main/register.html", context)

def register_company(request):
    form = CompanyForm(initial={'is_company': True, "is_private_person": False})

    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()


    context = {"form": form}
    return render(request, "main/register_company.html", context)

def register_private_person(request):
    form = PrivatePersonForm(initial={'is_company': False, "is_private_person": True})

    if request.method == "POST":
        form = PrivatePersonForm(request.POST)
        if form.is_valid():
            form.save()

    context = {"form": form}
    return render(request, "main/register_private_person.html", context)
