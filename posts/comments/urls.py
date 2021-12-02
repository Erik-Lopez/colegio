from django.urls import path, include

from . import views

# Erik, haz los comentarios para que se asemejen a los de reddit
urlpatterns = [
    path("<int:comment_id>/delete/", views.delete_comment, name='delete_comment'),
    path("create/", views.create_comment, name='create_comment'),
]
