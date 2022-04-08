from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import QuestionSerializer
from .models import Question


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
