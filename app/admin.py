from django.contrib import admin

from app.admins.choice_admin import ChoiceAdmin
from app.admins.client_user_admin import ClientUserAdmin
from app.admins.question_admin import QuestionAdmin
from app.modules.auth.models.client_user import ClientUser
from app.modules.polls.models.choice import Choice
from app.modules.polls.models.question import Question

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(ClientUser, ClientUserAdmin)
