import pytest

from polls.tests.test_factory import (
    QuestionFactory,
    AnswerFactory,
    MultiChoiceAnswerFactory,
)


@pytest.mark.django_db
def describe_base_text_model_str_method():
    def test_should_allow_question_model_to_stringify_using_text_property():
        question = QuestionFactory.create()

        assert str(question) == question.text

    def test_should_allow_answer_model_to_stringify_using_text_property():
        answer = AnswerFactory.create()

        assert str(answer) == answer.text

    def test_should_allow_multi_choice_answer_model_to_stringify_using_text_property():
        multi_choice_answer = MultiChoiceAnswerFactory.create()

        assert str(multi_choice_answer) == multi_choice_answer.text
