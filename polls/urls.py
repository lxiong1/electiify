from django.urls import path
from .views import QuestionViews

urlpatterns = [
    path("polls/questions", QuestionViews.as_view()),
    path("polls/questions/<int:question_id>", QuestionViews.as_view()),
]
