from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Exceptions
from django.db.utils import IntegrityError
# Models
from django.contrib.auth.models import User
from users.models import Profile

# Create your views here.
def login_view(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('posts')
        else:
            return render(request, 'users/login.html', {'title': 'Iniciar Sesión', 'error': "Credenciales inválidas. ¿Te has registrado?"})
    return render(request, 'users/login.html', {'title': 'Iniciar Sesión'})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        conf_pass = request.POST["password_confirmation"]

        if password != conf_pass:
            return render(request, 'users/signup.html', {'title': 'Registrarse', 'error': "Las contraseñas tienen que coincidir."})

        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(request, 'users/signup.html', {'title': 'Registrarse', 'error': "Este nombre ya está en uso."})
        profile = Profile(user=user)
        profile.save()

        login(request, user)
        return redirect('posts')
    return render(request, 'users/signup.html', {'title': 'Registrarse'})

def show_users(request, user_id = 0):
    if user_id == 0:
        profs = Profile.objects.order_by('-created_at')
        return render(request, 'users/users.html', {'profs': profs})

    try:
        prof = User.objects.get(pk=user_id)
        return render(request, 'users/user.html', {'prof': prof})
    except:
       return HttpResponse("El usuario no existe")
