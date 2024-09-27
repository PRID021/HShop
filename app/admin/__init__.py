from django.contrib import admin

from app.admin.choice_admin import ChoiceAdmin
from app.admin.question_admin import QuestionAdmin
from app.models.choice import Choice
from app.models.question import Question

# Register your models here.
admin.site.site_header = "MY SITE"


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
