from rest_framework.urls import path
from .views import QuestionView, AnswerView

QUESTIONS = "questions"
QUESTION_ID = "question_id"
ANSWERS = "answers"
ANSWER_ID = "answer_id"

QUESTIONS_PATH = f"{QUESTIONS}/"
QUESTION_ID_PATH = f"{QUESTIONS_PATH}<int:{QUESTION_ID}>/"
ANSWERS_PATH = f"{QUESTION_ID_PATH}{ANSWERS}/"
ANSWERS_ID_PATH = f"{ANSWERS_PATH}<int:{ANSWER_ID}>/"


urlpatterns = [
    path(QUESTIONS_PATH, QuestionView.as_view(), name=QUESTIONS),
    path(
        QUESTION_ID_PATH,
        QuestionView.as_view(),
        name=QUESTION_ID,
    ),
    path(ANSWERS_PATH, AnswerView.as_view(), name=ANSWERS),
    path(ANSWERS_ID_PATH, AnswerView.as_view(), name=ANSWER_ID),
]
