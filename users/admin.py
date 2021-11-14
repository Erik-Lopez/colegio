# Django
from django.contrib import admin

# Models
from users.models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user','profile_pic', 'created_at', 'last_modified')
    list_display_links = ('pk', 'user')
    list_editable = ['profile_pic']
    search_fields = ['created_at']
    list_filter = ['last_modified']

    fieldsets = (
            ('Profile', {
                'fields': ('user', 'pic'),
            }),
    )

