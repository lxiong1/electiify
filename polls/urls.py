from django.urls import path
from .views import QuestionView

POLLS = "polls"
QUESTIONS = "questions"
QUESTION_BY_ID = "question_by_id"
QUESTIONS_PATH = f"{POLLS}/{QUESTIONS}"

urlpatterns = [
    path(QUESTIONS_PATH, QuestionView.as_view(), name=QUESTIONS),
    path(
        f"{QUESTIONS_PATH}/<int:question_id>",
        QuestionView.as_view(),
        name=QUESTION_BY_ID,
    ),
]
