from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .constants import AnswerConstants, ChoiceConstants
from .serializers import QuestionSerializer, AnswerSerializer, ChoiceSerializer
from .models import Question, Answer, Choice


class QuestionView(APIView):
    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                data={"status": "error", "data": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer.save()

        return Response(
            data={"status": "success", "data": serializer.data},
            status=status.HTTP_201_CREATED,
        )

    def get(self, request, question_id=None):
        if question_id:
            question = get_object_or_404(Question, id=question_id)
            serializer = QuestionSerializer(question)

            return Response(
                data={"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)

        return Response(
            data={"status": "success", "data": serializer.data},
            status=status.HTTP_200_OK,
        )

    def patch(self, request, question_id=None):
        if not request.data:
            return Response(
                {"status": "success", "data": {}},
                status=status.HTTP_204_NO_CONTENT,
            )

        question = get_object_or_404(Question, id=question_id)
        serializer = QuestionSerializer(question, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

        return Response(
            {"status": "success", "data": {}},
            status=status.HTTP_204_NO_CONTENT,
        )

    def delete(self, request, question_id=None):
        question = get_object_or_404(Question, id=question_id)
        question.delete()

        return Response(
            {"status": "success", "data": f"Question '{question}' deleted"},
            status=status.HTTP_200_OK,
        )


class AnswerView(APIView):
    def post(self, request, question_id=None):
        question = get_object_or_404(Question, id=question_id)
        answer_text = request.data.get(AnswerConstants.TEXT)
        answer = question.answer_set.create(text=answer_text)
        serializer = AnswerSerializer(answer)

        return Response(
            data={"status": "success", "data": serializer.data},
            status=status.HTTP_201_CREATED,
        )

    def get(self, request, question_id=None, answer_id=None):
        if question_id and answer_id:
            answer = get_object_or_404(Answer, id=answer_id, question_id=question_id)
            serializer = AnswerSerializer(answer)

            return Response(
                data={"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

        answers = Answer.objects.filter(question_id=question_id)
        if not answers:
            return Response(
                data={"status": "error", "data": []},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = AnswerSerializer(answers, many=True)

        return Response(
            data={"status": "success", "data": serializer.data},
            status=status.HTTP_200_OK,
        )

    def patch(self, request, question_id=None, answer_id=None):
        if not request.data:
            return Response(
                {"status": "success", "data": {}},
                status=status.HTTP_204_NO_CONTENT,
            )

        answer = get_object_or_404(Answer, id=answer_id, question_id=question_id)
        serializer = AnswerSerializer(answer, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

        return Response(
            {"status": "success", "data": {}},
            status=status.HTTP_204_NO_CONTENT,
        )

    def delete(self, request, question_id=None, answer_id=None):
        answer = get_object_or_404(Answer, id=answer_id, question_id=question_id)
        answer.delete()

        return Response(
            {"status": "success", "data": f"Answer '{answer}' deleted"},
            status=status.HTTP_200_OK,
        )


class ChoiceView(APIView):
    def post(self, request, question_id=None):
        question = get_object_or_404(Question, id=question_id)
        choice_text = request.data.get(ChoiceConstants.TEXT)
        choice = question.choice_set.create(text=choice_text)
        serializer = ChoiceSerializer(choice)

        return Response(
            data={"status": "success", "data": serializer.data},
            status=status.HTTP_201_CREATED,
        )

    def get(self, request, question_id=None, choice_id=None):
        if question_id and choice_id:
            choice = get_object_or_404(Choice, id=choice_id, question_id=question_id)
            serializer = ChoiceSerializer(choice)

            return Response(
                data={"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

        choices = Choice.objects.filter(question_id=question_id)
        if not choices:
            return Response(
                data={"status": "error", "data": []},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = ChoiceSerializer(choices, many=True)

        return Response(
            data={"status": "success", "data": serializer.data},
            status=status.HTTP_200_OK,
        )

    def delete(self, request, question_id=None, choice_id=None):
        answer = get_object_or_404(Choice, id=choice_id, question_id=question_id)
        answer.delete()

        return Response(
            {"status": "success", "data": f"Answer '{answer}' deleted"},
            status=status.HTTP_200_OK,
        )
