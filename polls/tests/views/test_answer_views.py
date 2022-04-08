import pytest
from rest_framework import status
from rest_framework.reverse import reverse

import polls.urls
from polls.constants import AnswerConstants
from polls.tests.test_factory import QuestionFactory, AnswerFactory


@pytest.mark.django_db
def describe_answer_view_post_method():
    def test_should_return_201_status_code_when_answer_created_for_given_question(
        api_client, faker
    ):
        question = QuestionFactory.create()
        answer_text_to_post = f"{faker.text()}?"

        response = api_client.post(
            path=reverse(
                polls.urls.ANSWERS,
                kwargs={AnswerConstants.QUESTION_ID: question.id},
            ),
            data={AnswerConstants.TEXT: answer_text_to_post},
            format="json",
        )

        assert response.status_code == status.HTTP_201_CREATED

    def test_should_return_404_status_code_when_question_not_found_by_question_id(
        api_client, faker
    ):
        non_existent_question_id = faker.random_int()

        response = api_client.post(
            path=reverse(
                polls.urls.ANSWERS,
                kwargs={AnswerConstants.QUESTION_ID: non_existent_question_id},
            ),
            data={AnswerConstants.TEXT: f"{faker.text()}?"},
            format="json",
        )

        assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def describe_answer_view_get_method():
    def test_should_return_200_status_code_when_answers_retrieved_by_question_id(
        api_client,
    ):
        question = QuestionFactory.create()
        AnswerFactory.create()

        response = api_client.get(
            path=reverse(
                polls.urls.ANSWERS,
                kwargs={
                    AnswerConstants.QUESTION_ID: question.id,
                },
            ),
        )

        assert response.status_code == status.HTTP_200_OK

    def test_should_return_404_status_code_when_answers_not_found_by_question_id(
        api_client, faker
    ):
        non_existent_question_id = faker.random_int()

        response = api_client.get(
            path=reverse(
                polls.urls.ANSWERS,
                kwargs={
                    AnswerConstants.QUESTION_ID: non_existent_question_id,
                },
            ),
        )

        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_should_return_200_status_code_when_answer_found_by_question_and_answer_id(
        api_client,
    ):
        question = QuestionFactory.create()
        answer = AnswerFactory.create()

        response = api_client.get(
            path=reverse(
                polls.urls.ANSWER_ID,
                kwargs={
                    AnswerConstants.QUESTION_ID: question.id,
                    AnswerConstants.ANSWER_ID: answer.id,
                },
            ),
        )

        assert response.status_code == status.HTTP_200_OK

    def test_should_return_404_status_code_when_answer_not_found_by_question_and_answer_id(
        api_client, faker
    ):
        non_existent_question_id = faker.random_int()
        non_existent_answer_id = faker.random_int()

        response = api_client.get(
            path=reverse(
                polls.urls.ANSWER_ID,
                kwargs={
                    AnswerConstants.QUESTION_ID: non_existent_question_id,
                    AnswerConstants.ANSWER_ID: non_existent_answer_id,
                },
            ),
        )

        assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def describe_answer_view_patch_method():
    def test_should_return_204_status_code_when_request_payload_is_empty(
        api_client, faker
    ):
        any_question_id = faker.random_int()
        any_answer_id = faker.random_int()

        response = api_client.patch(
            path=reverse(
                polls.urls.ANSWER_ID,
                kwargs={
                    AnswerConstants.QUESTION_ID: any_question_id,
                    AnswerConstants.ANSWER_ID: any_answer_id,
                },
            ),
            data={},
            format="json",
        )

        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_should_return_200_status_code_when_answer_updated(api_client, faker):
        question = QuestionFactory.create()
        answer = AnswerFactory.create()
        answer_text_update = f"{faker.text()}?"

        response = api_client.patch(
            path=reverse(
                polls.urls.ANSWER_ID,
                kwargs={
                    AnswerConstants.QUESTION_ID: question.id,
                    AnswerConstants.ANSWER_ID: answer.id,
                },
            ),
            data={AnswerConstants.TEXT: answer_text_update},
            format="json",
        )

        assert response.status_code == status.HTTP_200_OK

    def test_should_return_404_status_code_when_answer_not_found_by_question_and_answer_id(
        api_client, faker
    ):
        non_existent_question_id = faker.random_int()
        non_existent_answer_id = faker.random_int()

        response = api_client.patch(
            path=reverse(
                polls.urls.ANSWER_ID,
                kwargs={
                    AnswerConstants.QUESTION_ID: non_existent_question_id,
                    AnswerConstants.ANSWER_ID: non_existent_answer_id,
                },
            ),
            data={AnswerConstants.TEXT: f"{faker.text()}?"},
            format="json",
        )

        assert response.status_code == status.HTTP_404_NOT_FOUND
