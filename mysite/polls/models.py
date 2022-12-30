from django.db import models

# Each model is a subclass of django.db.models.Model
# Left side represents field and db column name
# First arg to the models.xxx() is if a human readable name is needed (ex. date published)-- optional

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

# Each choice is tied to a question via fKey

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)