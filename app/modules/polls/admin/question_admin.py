from django.contrib import admin

from app.models import Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    max_num = 3
    classes = ["collapse"]
    verbose_name = "Choice"
    verbose_name_plural = "Choices"

    class Media:
        css = {"all": ("polls/styles/admin.css",)}


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
    list_per_page = 15
    inlines = [ChoiceInline]
