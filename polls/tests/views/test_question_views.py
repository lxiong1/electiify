import pytest
from rest_framework import status
from rest_framework.reverse import reverse

import polls.urls
from polls.constants import QuestionConstants, AnswerConstants
from polls.tests.test_factory import QuestionFactory, AnswerFactory


@pytest.mark.django_db
def describe_question_view_post_method():
    def test_should_return_201_status_code_when_request_payload_serializable(
        api_client, faker
    ):
        question_text_to_post = f"{faker.text()}?"

        response = api_client.post(
            path=reverse(polls.urls.QUESTIONS),
            data={QuestionConstants.TEXT: question_text_to_post},
            format="json",
        )

        assert response.status_code == status.HTTP_201_CREATED

    def test_should_return_400_status_code_when_request_payload_is_empty(api_client):
        response = api_client.post(
            path=reverse(polls.urls.QUESTIONS), data={}, format="json"
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    @pytest.mark.parametrize(
        "invalid_dict_key",
        [
            "",
            " ",
            "invalid",
        ],
    )
    def test_should_return_400_status_code_when_request_payload_dict_key_not_question_property(
        api_client, invalid_dict_key, faker
    ):
        response = api_client.post(
            path=reverse(polls.urls.QUESTIONS),
            data={invalid_dict_key: f"{faker.text()}?"},
            format="json",
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    @pytest.mark.parametrize(
        "invalid_dict_value",
        [
            {},
            [],
            (),
            True,
            None,
        ],
    )
    def test_should_return_400_status_code_when_request_payload_dict_value_not_str_or_number(
        api_client, invalid_dict_value
    ):
        response = api_client.post(
            path=reverse(polls.urls.QUESTIONS),
            data={QuestionConstants.TEXT: invalid_dict_value},
            format="json",
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def describe_question_view_get_method():
    def test_should_return_200_status_code_when_request_has_no_question_id(
        api_client,
    ):
        response = api_client.get(path=reverse(polls.urls.QUESTIONS))

        assert response.status_code == status.HTTP_200_OK

    def test_should_return_200_status_code_when_request_has_question_id(
        api_client,
    ):
        question = QuestionFactory.create()

        response = api_client.get(
            path=reverse(
                polls.urls.QUESTION_ID,
                kwargs={QuestionConstants.QUESTION_ID: question.id},
            ),
            format="json",
        )

        assert response.status_code == status.HTTP_200_OK

    def test_should_return_404_status_code_when_request_has_non_existent_question_id(
        api_client, faker
    ):
        non_existent_question_id = faker.random_int()

        response = api_client.get(
            path=reverse(
                polls.urls.QUESTION_ID,
                kwargs={QuestionConstants.QUESTION_ID: non_existent_question_id},
            ),
            format="json",
        )

        assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def describe_question_view_patch_method():
    def test_should_return_204_status_code_when_request_payload_is_empty(
        api_client,
    ):
        response = api_client.patch(
            path=reverse(polls.urls.QUESTIONS),
            data={},
            format="json",
        )

        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_should_return_200_status_code_when_request_payload_is_update_to_existing_question(
        api_client, faker
    ):
        question = QuestionFactory.create()
        question_text_update = f"{faker.text()}?"

        response = api_client.patch(
            path=reverse(
                polls.urls.QUESTION_ID,
                kwargs={QuestionConstants.QUESTION_ID: question.id},
            ),
            data={QuestionConstants.TEXT: question_text_update},
            format="json",
        )

        assert response.status_code == status.HTTP_200_OK

    def test_should_return_404_status_code_when_question_does_not_exist(
        api_client, faker
    ):
        non_existent_question_id = faker.random_int()

        response = api_client.patch(
            path=reverse(
                polls.urls.QUESTION_ID,
                kwargs={QuestionConstants.QUESTION_ID: non_existent_question_id},
            ),
            data={QuestionConstants.TEXT: f"{faker.text()}?"},
            format="json",
        )

        assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def describe_question_view_delete_method():
    def test_should_return_200_status_code_when_request_payload_is_update_to_existing_question(
        api_client,
    ):
        question = QuestionFactory.create()

        response = api_client.delete(
            path=reverse(
                polls.urls.QUESTION_ID,
                kwargs={QuestionConstants.QUESTION_ID: question.id},
            ),
        )

        assert response.status_code == status.HTTP_200_OK

    def test_should_return_404_status_code_when_question_does_not_exist(
        api_client, faker
    ):
        non_existent_question_id = faker.random_int()

        response = api_client.delete(
            path=reverse(
                polls.urls.QUESTION_ID,
                kwargs={QuestionConstants.QUESTION_ID: non_existent_question_id},
            ),
        )

        assert response.status_code == status.HTTP_404_NOT_FOUND
