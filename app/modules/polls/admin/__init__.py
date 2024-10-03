from django.contrib import admin

from app.modules.polls.admin import question_admin
from app.modules.polls.admin.choice_admin import ChoiceAdmin
from app.modules.polls.models.choice import Choice
from app.modules.polls.models.question import Question

# Register your models here.
admin.site.site_header = "MY SITE"


admin.site.register(Question, question_admin)
admin.site.register(Choice, ChoiceAdmin)
