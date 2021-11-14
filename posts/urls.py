from django.urls import path

from . import views

urlpatterns = [
    path("", views.show_posts),
    path("create/", create_post)
]
