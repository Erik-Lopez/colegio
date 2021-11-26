from django.urls import path

from . import views

urlpatterns = [
    path("", views.show_clubs, name='clubs'),
    path("<int:club_id>/", views.show_clubs, name='clubs'),
    path("<int:club_id>/delete/", views.delete_club, name='delete_club'),
    path("<int:club_id>/join/", views.join_club, name='join_club'),
    path("<int:club_id>/leave/", views.leave_club, name='leave_club'), 
    path("create/", views.create_club, name='create_club'),
]
