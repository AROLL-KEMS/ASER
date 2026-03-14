from django.shortcuts import render, redirect
from .models import *

def home(request):
    return render(request, 'LearnHub/home.html')


def events(request):
    return render(request, 'LearnHub/events.html')

def contact(request):
    message = ""
    if request.method == "POST":
        #Check Honeypot
        if request.POST.get('honeypot'):
            return redirect('contact')
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        contact = contacts.objects.create(
            name = name,
            email = email,
            phone = phone,
            message = message
        )
        if contact:
            message = "Your mail was send successfully"
    
    return render(request, 'LearnHub/contact.html', {'message':message})

