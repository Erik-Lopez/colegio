from django.urls import path

from . import views

urlpatterns = [
    path("", views.show_posts),
    path("create/", views.create_post)
]
