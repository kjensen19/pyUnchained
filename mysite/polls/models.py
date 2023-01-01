import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin

# Each model is a subclass of django.db.models.Model
# Left side represents field and db column name
# First arg to the models.xxx() is if a human readable name is needed (ex. date published)-- optional

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

# Each choice is tied to a question via fKey

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text