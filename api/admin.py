from django.contrib import admin
from django.contrib.auth.models import Group
from .models import CustomUser, Media

# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'created_at', 'updated_at')
    search_fields = ('username', 'email')


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'media_file', 'file_type', 'file_size',
                    'user', 'is_public', 'is_deleted', 'created_at', 'updated_at')
    list_filter = ('file_type', 'is_public', 'is_deleted', 'user')
    search_fields = ('title', 'description', 'file_type')


admin.site.unregister(Group)
