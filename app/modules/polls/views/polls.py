from typing import Any

from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import path
from django.utils import timezone
from django.views import generic

from app.modules.polls.models.question import Question


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self) -> QuerySet[Question]:
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by(
            "-pub_date"
        )[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/question_detail.html"

    """
    Excludes any questions that aren't published yet.
    """

    def get_queryset(self) -> QuerySet[Any]:
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request: HttpRequest, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.method == "POST":
        selected_choice_id = request.POST.get("choice")
        if selected_choice_id:
            selected_choice = question.choice_set.get(pk=selected_choice_id)
            selected_choice.votes += 1
            selected_choice.save()
            return redirect("results", pk=question.id)

    return HttpResponse("You're voting on question %s. " % question_id)
