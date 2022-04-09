import pytest
from rest_framework import status
from rest_framework.reverse import reverse

import polls.urls
from polls.constants import ChoiceConstants
from polls.tests.test_factory import QuestionFactory, ChoiceFactory


@pytest.mark.django_db
def describe_choice_view_post_method():
    def test_should_return_201_status_code_when_choice_created_for_given_question(
        api_client, faker
    ):
        question = QuestionFactory.create()
        choice_text_to_post = f"{faker.text()}?"

        response = api_client.post(
            path=reverse(
                polls.urls.CHOICES,
                kwargs={ChoiceConstants.QUESTION_ID: question.id},
            ),
            data={ChoiceConstants.TEXT: choice_text_to_post},
            format="json",
        )

        assert response.status_code == status.HTTP_201_CREATED

    def test_should_return_404_status_code_when_question_not_found_by_question_id(
        api_client, faker
    ):
        non_existent_question_id = faker.random_int()

        response = api_client.post(
            path=reverse(
                polls.urls.CHOICES,
                kwargs={ChoiceConstants.QUESTION_ID: non_existent_question_id},
            ),
            data={ChoiceConstants.TEXT: f"{faker.text()}?"},
            format="json",
        )

        assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def describe_choice_view_get_method():
    def test_should_return_200_status_code_when_choices_retrieved_by_question_id(
        api_client,
    ):
        question = QuestionFactory.create()
        ChoiceFactory.create()

        response = api_client.get(
            path=reverse(
                polls.urls.CHOICES,
                kwargs={
                    ChoiceConstants.QUESTION_ID: question.id,
                },
            ),
        )

        assert response.status_code == status.HTTP_200_OK

    def test_should_return_404_status_code_when_choices_not_found_by_question_id(
        api_client, faker
    ):
        non_existent_question_id = faker.random_int()

        response = api_client.get(
            path=reverse(
                polls.urls.CHOICES,
                kwargs={
                    ChoiceConstants.QUESTION_ID: non_existent_question_id,
                },
            ),
        )

        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_should_return_200_status_code_when_choice_found_by_question_and_choice_id(
        api_client,
    ):
        question = QuestionFactory.create()
        choice = ChoiceFactory.create()

        response = api_client.get(
            path=reverse(
                polls.urls.CHOICE_ID,
                kwargs={
                    ChoiceConstants.QUESTION_ID: question.id,
                    ChoiceConstants.CHOICE_ID: choice.id,
                },
            ),
        )

        assert response.status_code == status.HTTP_200_OK

    def test_should_return_404_status_code_when_choice_not_found_by_question_and_choice_id(
        api_client, faker
    ):
        non_existent_question_id = faker.random_int()
        non_existent_choice_id = faker.random_int()

        response = api_client.get(
            path=reverse(
                polls.urls.CHOICE_ID,
                kwargs={
                    ChoiceConstants.QUESTION_ID: non_existent_question_id,
                    ChoiceConstants.CHOICE_ID: non_existent_choice_id,
                },
            ),
        )

        assert response.status_code == status.HTTP_404_NOT_FOUND
