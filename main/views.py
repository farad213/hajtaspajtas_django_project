from django.shortcuts import render

def home(request):
    return render(request, "main/home.html", {})

def prices(request):
    return render(request, "main/prices.html", {})

def online_order(request):
    return render(request, "main/online_order.html", {})

def contact(request):
    return render(request, "main/conatct.html", {})

def about_us(request):
    return render(request, "main/about_us.html", {})

def budapest(request):
    return render(request, "main/budapest.html", {})

def videk(request):
    return render(request, "main/videk.html", {})

def kulfold(request):
    return render(request, "main/kulfold.html", {})
