from rest_framework.urls import path
from .views import QuestionView

QUESTIONS = "questions"
QUESTION_ID = "question_id"

urlpatterns = [
    path(QUESTIONS, QuestionView.as_view(), name=QUESTIONS),
    path(
        f"{QUESTIONS}/<int:{QUESTION_ID}>",
        QuestionView.as_view(),
        name=QUESTION_ID,
    ),
]
