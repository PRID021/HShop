from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .models import Question


def index(request: HttpRequest):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(
        template_name="polls/index.html",
        context=context,
        request=request,
    )


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(
        request=request,
        template_name="polls/question_detail.html",
        context={"question": question},
    )


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(
        request=request,
        template_name="polls/results.html",
        context={"question": question},
    )


def vote(request: HttpRequest, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.method == "POST":
        selected_choice_id = request.POST.get("choice")
        if selected_choice_id:
            selected_choice = question.choice_set.get(pk=selected_choice_id)
            selected_choice.votes += 1
            selected_choice.save()
            return redirect("results", question_id=question.id)

    return HttpResponse("You're voting on question %s. " % question_id)
