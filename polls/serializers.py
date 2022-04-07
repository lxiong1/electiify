from rest_framework import serializers
from .models import Question, Answer, MultiChoiceAnswer


class QuestionSerializer(serializers.ModelSerializer):
    text = serializers.CharField(max_length=200)

    class Meta:
        model = Question
        fields = "__all__"


class AnswerSerializer(serializers.ModelSerializer):
    question = serializers.CharField(max_length=200)
    text = serializers.CharField(max_length=200)

    class Meta:
        model = Answer
        fields = "__all__"


class MultiChoiceAnswerSerializer(serializers.ModelSerializer):
    question = serializers.CharField(max_length=200)
    text = serializers.CharField(max_length=200)
    votes = serializers.IntegerField(required=False, default=0)

    class Meta:
        model = MultiChoiceAnswer
        fields = "__all__"
