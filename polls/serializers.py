from rest_framework import serializers

from .constants import AnswerConstants, ChoiceConstants
from .models import Question, Answer, Choice


class QuestionSerializer(serializers.ModelSerializer):
    text = serializers.CharField(max_length=200)

    class Meta:
        model = Question
        fields = "__all__"


class AnswerSerializer(serializers.ModelSerializer):
    question_id = serializers.IntegerField(required=True)
    text = serializers.CharField(max_length=200)

    class Meta:
        model = Answer
        fields = [AnswerConstants.ID, AnswerConstants.QUESTION_ID, AnswerConstants.TEXT]


class ChoiceSerializer(serializers.ModelSerializer):
    question_id = serializers.IntegerField(required=True)
    text = serializers.CharField(max_length=200)
    votes = serializers.IntegerField(required=False, default=0)

    class Meta:
        model = Choice
        fields = [
            ChoiceConstants.ID,
            ChoiceConstants.QUESTION_ID,
            ChoiceConstants.TEXT,
            ChoiceConstants.VOTES,
        ]
