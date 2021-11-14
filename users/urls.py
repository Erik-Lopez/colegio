from django.urls import path

from . import views

urlpatterns = [
    path("", views.show_users),
    path("create/", views.create_user)
]
