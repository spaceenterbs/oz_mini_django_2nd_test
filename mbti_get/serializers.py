from rest_framework import serializers
from .models import Answer, Result


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["id", "contents", "choices"]


class ResultSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer()

    # answer = serializers.PrimaryKeyRelatedField(queryset=Answer.objects.all())
    class Meta:
        model = Result
        fields = ["id", "mbti_result"]
