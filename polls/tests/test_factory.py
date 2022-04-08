import factory
from faker import Faker

from polls.constants import (
    QuestionConstants,
    AnswerConstants,
    MultiChoiceAnswerConstants,
)
from polls.models import Question, Answer, MultiChoiceAnswer

faker = Faker()


class QuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Question
        django_get_or_create = (QuestionConstants.TEXT,)

    text = f"{faker.text()}?"


class AnswerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Answer
        django_get_or_create = (
            AnswerConstants.TEXT,
            AnswerConstants.QUESTION,
        )

    text = f"{faker.text()}?"
    question = factory.SubFactory(QuestionFactory)


class MultiChoiceAnswerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MultiChoiceAnswer
        django_get_or_create = (
            MultiChoiceAnswerConstants.TEXT,
            MultiChoiceAnswerConstants.QUESTION,
            MultiChoiceAnswerConstants.VOTES,
        )

    text = f"{faker.text()}?"
    question = factory.SubFactory(QuestionFactory)
    votes = faker.random_int(0, 100)
