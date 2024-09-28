# polls/urls.py
from django.urls import path
from . import polls as polls_views

urlpatterns = [
    path("", polls_views.IndexView.as_view(), name="index"),
    path("<int:pk>/", polls_views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", polls_views.ResultView.as_view(), name="results"),
    path("<int:question_id>/vote/", polls_views.vote, name="vote"),
]
