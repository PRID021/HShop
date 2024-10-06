from django.contrib import admin

from app.modules.polls.models.choice import Choice


class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Question", {"fields": ["question"]}),
        ("Choice text", {"fields": ["choice_text"]}),
        ("Votes", {"fields": ["votes"]}),
    ]

    list_per_page = 15
