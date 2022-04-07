from django.db import models


class Session(models.Model):
    created_at = models.DateTimeField()


class Text(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

    class Meta:
        abstract = True


class Question(Text):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)


class Answer(Text):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class MultiChoiceAnswer(Text):
    votes = models.IntegerField(default=0)
    multi_choice_question = models.ForeignKey(Question, on_delete=models.CASCADE)
