import factory
from faker import Faker

from polls.models import Question, Answer, MultiChoiceAnswer

TEXT = "text"
QUESTION = "question"
VOTES = "votes"

faker = Faker()


class QuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Question
        django_get_or_create = (TEXT,)

    text = f"{faker.text()}?"


class AnswerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Answer
        django_get_or_create = (
            TEXT,
            QUESTION,
        )

    text = f"{faker.text()}?"
    question = factory.SubFactory(QuestionFactory)


class MultiChoiceAnswerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MultiChoiceAnswer
        django_get_or_create = (
            TEXT,
            QUESTION,
            VOTES,
        )

    text = f"{faker.text()}?"
    question = factory.SubFactory(QuestionFactory)
    votes = faker.random_int(0, 100)
