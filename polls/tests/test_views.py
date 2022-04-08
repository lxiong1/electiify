import pytest
from rest_framework import status
from rest_framework.reverse import reverse

import polls.urls
from polls.tests.test_factory import QuestionFactory


@pytest.mark.django_db
def describe_question_view_post_method():
    def test_should_return_201_status_code_when_request_payload_serializable(
        api_client,
    ):
        response = api_client.post(
            path=reverse(polls.urls.QUESTIONS),
            data={"text": "What's your full name?"},
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
        api_client, invalid_dict_key
    ):
        response = api_client.post(
            path=reverse(polls.urls.QUESTIONS),
            data={invalid_dict_key: "What's your full name?"},
            format="json",
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    @pytest.mark.parametrize(
        "invalid_dict_value",
        [
            123,
            123.123,
            True,
        ],
    )
    def test_should_return_400_status_code_when_request_payload_dict_value_not_string(
        api_client, invalid_dict_value
    ):
        response = api_client.post(
            path=reverse(polls.urls.QUESTIONS),
            data={invalid_dict_value: "What's your full name?"},
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

    def test_should_return_200_status_code_when_request_has_specified_question_id(
        api_client,
    ):
        question = QuestionFactory.create()

        response = api_client.get(
            path=reverse(polls.urls.QUESTION_ID, kwargs={"question_id": question.id})
        )

        assert response.status_code == status.HTTP_200_OK

    def test_should_return_404_status_code_when_request_has_specified_question_id_that_does_not_exist(
        api_client,
    ):
        non_existent_question_id = 1

        response = api_client.get(
            path=reverse(
                polls.urls.QUESTION_ID, kwargs={"question_id": non_existent_question_id}
            )
        )

        assert response.status_code == status.HTTP_404_NOT_FOUND
