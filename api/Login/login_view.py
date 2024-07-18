# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken
from datetime import timedelta

def login_sesion(request):
    template_name = 'Accesos/login.html'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirigir a la página de inicio u otra página
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, template_name)

def generate_token_view(request):
    # Asegúrate de autenticar al usuario antes de generar el token
    user = User.objects.first()  # Aquí deberías autenticar al usuario de manera adecuada

    # Genera un token de acceso con una duración de 24 horas
    token = AccessToken.for_user(user)
    token.set_exp(lifetime=timedelta(hours=24))

    # Crear la URL de acceso con el token generado
    access_url = f"http://127.0.0.1:8000/home_token/?token={token}"

    return render(request, 'Accesos/generate_token.html', {'access_url': access_url})

