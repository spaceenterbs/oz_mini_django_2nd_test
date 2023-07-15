from rest_framework import serializers
from .models import Answer, Result


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            "id",
            "choices",
            "contents",
        ]
        # fields = ("contents", "choices",)
        # fields = "__all__"


class ResultSerializer(serializers.ModelSerializer):
    # answer = serializers.PrimaryKeyRelatedField(queryset=Answer.objects.all())
    class Meta:
        model = Result
        fields = [
            "id",
            "mbti_result",
        ]
        # fields = ('mbti_result",)
        # fields = "__all__",
