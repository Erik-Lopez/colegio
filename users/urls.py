from django.urls import path

from . import views

urlpatterns = [
    path("", views.show_users),
    path("create/", views.create_user),

    path("signup/", views.signup),
    path("login/", views.login_view, name='login'),
    path("logout/", views.logout_view, name='logout')
]
