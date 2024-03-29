import factory
from faker import Faker

from polls.constants import (
    QuestionConstants,
    AnswerConstants,
    ChoiceConstants,
)
from polls.models import Question, Answer, Choice

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


class ChoiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Choice
        django_get_or_create = (
            ChoiceConstants.TEXT,
            ChoiceConstants.QUESTION,
            ChoiceConstants.VOTES,
        )

    text = f"{faker.text()}?"
    question = factory.SubFactory(QuestionFactory)
    votes = faker.random_int()
