from django.db import models
from common.models import CommonModel


class Answer(CommonModel):
    contents = models.CharField(max_length=255)
    choices = models.CharField(max_length=1)  # 예를 들어, "I" 또는 "E"


class Result(CommonModel):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    mbti_result = models.CharField(max_length=4)  # 예를 들어, "INFP"
