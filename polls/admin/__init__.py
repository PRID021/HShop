from django.contrib import admin

from polls.admin.choice_admin import ChoiceAdmin
from polls.admin.question_admin import QuestionAdmin
from polls.models import Choice, Question

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
