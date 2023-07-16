from django.db import models
from django.db.models import JSONField  # Django 3.1 이상에서는 django.db.models에서 import 가능
from common.models import CommonModel


class Answer(CommonModel):
    choices = JSONField()  # 예: ["I", "E", "N", ...]
    contents = JSONField()  # 예: ["여긴 나만 알고 싶어! 다이어리에 끄적여놓는다.", "사려고 했던 물건들", ...]

    def __str__(self):
        return f"{self.choices} - {self.contents}"


class Result(CommonModel):
    # answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True)
    mbti_result = models.CharField(max_length=1000)  # 예: "INFP"

    def __str__(self):
        return self.mbti_result


# from django.db import models
# from common.models import CommonModel

# # from django.contrib.postgres.fields import ArrayField


# # class Choice(CommonModel):
# #     choice = models.CharField(max_length=1000)


# # class Content(CommonModel):
# #     content = models.CharField(max_length=255)


# # class Answer(CommonModel):
# #     choices = models.ManyToManyField(Choice)
# #     contents = models.ManyToManyField(Content)

# # class Answer(CommonModel):
# #     choices = ArrayField(models.CharField(max_length=1000))  # "I" 또는 "E" 등의 배열
# #     contents = ArrayField(models.CharField(max_length=255))  # 컨텐츠 배열
# # from django.db import models
# # from common.models import CommonModel


# class Answer(CommonModel):
#     choices = models.CharField(max_length=1000)  # 예를 들어, "I" 또는 "E"

#     contents = models.CharField(max_length=1000)

#     # def __str__(self) -> str:
#     #     return f"{self.choices} - {self.contents}"


# class Result(CommonModel):
#     # answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
#     mbti_result = models.CharField(max_length=1000)  # 예를 들어, "INFP"

#     # def __str__(self) -> str:
#     #     return self.mbti_result
