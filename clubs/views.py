from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from clubs.models import Club

def show_clubs(request, club_id=0):
    if club_id == 0:
        clubs = Club.objects.order_by('-created_at')
        return render(request, 'clubs/clubs.html', {'clubs': clubs})
    try:
        club = Club.objects.get(pk=club_id)
        user_in_club = False
        if request.user.is_authenticated:
            if club in request.user.profile.clubs.all() or club.owner == request.user:
                user_in_club = True
        return render(request, 'clubs/club.html', {'club': club, 'user_in_club': user_in_club})
    except:
        return HttpResponse("El club no existe")

@login_required(login_url='login')
def create_club(request):
    if request.method == 'POST':
        name = request.POST["name"]
        owner = request.user
        logo = request.FILES["logo"]
        description = request.POST["description"]

        club = Club(name=name, owner=owner, logo=logo, description=description)
        club.save()

        club_id = club.pk
        
        return redirect('clubs', club_id=club_id)
    return render(request, 'clubs/create_club.html')

@login_required(login_url='login')
def delete_club(request, club_id):
    try:
        club = Club.objects.get(pk=club_id)
    except:
        HttpResponse("El club no existe")
    if request.user.pk != club.owner.pk:
        return HttpResponse("No tienes permiso para hacer esto")
    club.delete()
    return redirect('clubs')

@login_required(login_url='login')
def join_club(request, club_id):
    try:
        club = Club.objects.get(pk=club_id)
    except:
        return HttpResponse("El club no existe")
    if request.user == club.owner or request.user in club.profile_set.all():
        return HttpResponse("<h1 style='text-align:center;'>NO PODÉS</h1>")

    club.profile_set.add(request.user.profile) 
    club.save()
    return redirect('clubs', club_id=club_id)

@login_required(login_url='login')
def leave_club(request, club_id):
    try:
        club = Club.objects.get(pk=club_id)
    except:
        return HttpResponse("El club no existe")
    if request.user == club.owner or request.user.profile not in club.profile_set.all():
        return HttpResponse("<h1 style='text-align:center;'>NO PODÉS</h1>")

    club.profile_set.remove(request.user.profile)
    club.save()

    return redirect('clubs', club_id=club_id)
