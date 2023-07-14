# myapp/urls.py
from django.urls import path
from .views import AnswerListCreate, ResultListCreate

urlpatterns = [
    path("answers/", AnswerListCreate.as_view(), name="answer-list"),
    path("results/", ResultListCreate.as_view(), name="result-list"),
]
