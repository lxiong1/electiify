from rest_framework import serializers

from .constants import AnswerConstants, MultiChoiceAnswerConstants
from .models import Question, Answer, MultiChoiceAnswer


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


class MultiChoiceAnswerSerializer(serializers.ModelSerializer):
    question_id = serializers.IntegerField(required=True)
    text = serializers.CharField(max_length=200)
    votes = serializers.IntegerField(required=False, default=0)

    class Meta:
        model = MultiChoiceAnswer
        fields = [
            MultiChoiceAnswerConstants.ID,
            MultiChoiceAnswerConstants.QUESTION_ID,
            MultiChoiceAnswerConstants.TEXT,
            MultiChoiceAnswerConstants.VOTES,
        ]
