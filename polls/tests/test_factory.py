import factory
from faker import Faker

from polls.models import Question


TEXT = "text"
faker = Faker()


class QuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Question
        django_get_or_create = (TEXT,)

    text = f"{faker.text()}?"
