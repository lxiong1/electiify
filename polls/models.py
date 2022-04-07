from django.db import models


class BaseText(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

    class Meta:
        abstract = True


class Question(BaseText):
    pass


class Answer(BaseText):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class MultiChoiceAnswer(BaseText):
    multi_choice_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
