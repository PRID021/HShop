import datetime

from django.db import models
from django.utils import timezone

from .question import Question

# Create your models here.


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text

    class Meta:
        app_label = "polls"
