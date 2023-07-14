from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Answer, Result
from .serializers import AnswerSerializer, ResultSerializer


class AnswerListCreate(APIView):
    def get(self, request):
        answers = Answer.objects.all()
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResultListCreate(APIView):
    def get(self, request):
        results = Result.objects.all()
        serializer = ResultSerializer(results, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# from rest_framework import generics
# from .models import Answer, Result
# from .serializers import AnswerSerializer, ResultSerializer


# class AnswerListCreate(generics.ListCreateAPIView):
#     queryset = Answer.objects.all()
#     serializer_class = AnswerSerializer


# class ResultListCreate(generics.ListCreateAPIView):
#     queryset = Result.objects.all()
#     serializer_class = ResultSerializer


# # from django.shortcuts import render
