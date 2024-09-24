from django.contrib import admin


class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Question", {"fields": ["question"]}),
        ("Choice text", {"fields": ["choice_text"]}),
        ("Votes", {"fields": ["votes"]}),
    ]
    list_per_page = 15
