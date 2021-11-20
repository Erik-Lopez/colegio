from django.urls import path

from . import views

urlpatterns = [
    path("", views.show_posts, name='posts'),
    path("<int:post_id>/", views.show_posts, name='posts'),
    path("<int:post_id>/delete/", views.delete_post, name='delete_post'),
    path("create/", views.create_post, name='create_post'),
]
