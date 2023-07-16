from rest_framework import serializers
from .models import Answer, Result  # Content, Choice


# class AnswerSerializer(serializers.ModelSerializer):
#     choices = serializers.ListField(child=serializers.CharField(max_length=1000))
#     contents = serializers.ListField(child=serializers.CharField(max_length=255))

#     class Meta:
#         model = Answer
#         fields = ["choices", "contents"]

#     def create(self, validated_data):
#         choices_data = validated_data.pop("choices")
#         contents_data = validated_data.pop("contents")

#         answer = Answer.objects.create(**validated_data)

#         for choice_data in choices_data:
#             Choice.objects.create(answer=answer, choice=choice_data)
#         for content_data in contents_data:
#             Content.objects.create(answer=answer, content=content_data)

#         return answer


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
