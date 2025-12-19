from django.contrib import admin

from tasks.models import Task, Tag


# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_filter = ("content",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_filter = ("name",)
