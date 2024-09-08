from django.contrib import admin
from .models import Task, Tag, TaskTag

# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'due_date',
                    'created_at', 'updated_at', 'user')
    list_filter = ('status', 'due_date', 'user')
    search_fields = ('title', 'description')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(TaskTag)
class TaskTagAdmin(admin.ModelAdmin):
    list_display = ('task', 'tag')
