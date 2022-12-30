import datetime
from django.db import models
from django.utils import timezone

# Each model is a subclass of django.db.models.Model
# Left side represents field and db column name
# First arg to the models.xxx() is if a human readable name is needed (ex. date published)-- optional

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# Each choice is tied to a question via fKey

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text