from django.shortcuts import render

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

