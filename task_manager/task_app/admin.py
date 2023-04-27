# Register your models here.
from django.contrib import admin

from .models import Task, TaskStatus, Author


@admin.register(Task)
class Task(admin.ModelAdmin):
    pass


@admin.register(Author)
class Task(admin.ModelAdmin):
    pass


@admin.register(TaskStatus)
class Task(admin.ModelAdmin):
    pass
