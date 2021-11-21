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
        return render(request, 'clubs/club.html', {'club': club})
    except:
        return HttpResponse("El club no existe")

@login_required(login_url='login')
def create_club(request):
    if request.method == 'POST':
        name = request.POST["name"]
        owner = request.user
        logo = request.FILES["logo"]
        description = request.POST["description"]

        club = Club(name=name, owner=owner, logo=logo)
        club.save()

        club_id = club.pk
        
        return redirect('clubs', club_id=club_id)
    return render(request, 'clubs/create_club.html')

@login_required
def delete_club(request, club_id):
    try:
        club = Club.objects.get(pk=club_id)
    except:
        HttpResponse("El club no existe")
    if request.user.pk != club.owner.pk:
        return HttpResponse("No tienes permiso para hacer esto")
    club.delete()
    return redirect('clubs')
