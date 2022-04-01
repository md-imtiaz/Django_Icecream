from django.shortcuts import render

from datetime import datetime
from .models import Contact
from django.contrib import messages

# Create your views here.
from django.shortcuts import HttpResponse

def index(request):
    context = {
        "variable1": "ALHUMDULILAH!",
        "variable2": "SULLALAHUALAIHIWASULAM"
    }
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, phone=phone, message=message, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent successfuly! ')
    return render(request,'contact.html')