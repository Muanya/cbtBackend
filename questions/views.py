from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from questions.models import Choice, Question
from questions.serializers import QuestionSerializer, ChoiceSerializer


class QuestionView(APIView):
    def post(self, req):
        serializer = QuestionSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, req):
        try:
            x = int(req.query_params['limit'])
        except MultiValueDictKeyError:
            x = 10  # default value when no values is given
        except ValueError as e:
            return Response({'msg': 'Invalid value for key'}, status=status.HTTP_400_BAD_REQUEST)

        # TODO: filter based on year/session
        questions = Question.objects.all()[:x]
        res = []
        for ques in questions:
            res.append(QuestionSerializer(ques).data)
        return Response(res)


class ChoiceView(APIView):
    def post(self, req):
        serializer = ChoiceSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, req):
        try:
            x = int(req.query_params['id'])
        except MultiValueDictKeyError:
            x = 1  # default value when no values is given
        except ValueError as e:
            return Response({'msg': 'Invalid value for key'}, status=status.HTTP_400_BAD_REQUEST)
        choices = Choice.objects.filter(question=x)
        res = []
        for choice in choices:
            res.append(ChoiceSerializer(choice).data)
        return Response(res)
