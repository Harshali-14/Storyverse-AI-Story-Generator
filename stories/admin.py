from django.contrib import admin
from .models import Story


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "title",
        "character",
        "theme",
        "created_at"
    )

    search_fields = (
        "title",
        "character",
        "keyword",
        "theme"
    )

    list_filter = (
        "theme",
        "created_at"
    )