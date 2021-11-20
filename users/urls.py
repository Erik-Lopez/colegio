from django.urls import path

from . import views

urlpatterns = [
    path("", views.show_users, name='show_users'),
    path("<int:user_id>/", views.show_users, name='show_users'),

    path("signup/", views.signup, name='signup'),
    path("login/", views.login_view, name='login'),
    path("logout/", views.logout_view, name='logout')
]
