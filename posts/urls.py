from django.urls import path

from . import views

urlpatterns = [
    path("", views.show_posts, name='posts'),
    path("<int:post_id>/", views.show_posts, name='posts'),
    path("create/", views.create_post, name='create_post')
]
