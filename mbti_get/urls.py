from django.urls import path
from .views import AnswerListCreate, ResultListCreate, CountResult

urlpatterns = [
    path(
        "answers/",
        AnswerListCreate.as_view(),
        name="answer-list",
    ),
    path(
        "results/",
        ResultListCreate.as_view(),
        name="result-list",
    ),
    path(
        "count/",
        CountResult.as_view(),
        name="count",
    ),
]
