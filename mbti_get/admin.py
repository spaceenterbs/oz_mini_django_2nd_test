from django.contrib import admin
from .models import Answer, Result


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass
    # list_display = ("id", "contents", "choices")


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    pass
    # list_display = ("id", "answer", "mbti_result")
