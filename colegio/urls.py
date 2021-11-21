from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path("posts/", include("posts.urls"), name='posts'),
    path("users/", include("users.urls"), name='users'),
    path("clubs/", include("clubs.urls"), name='clubs'),
    path("admin/", admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
