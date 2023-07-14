from django.db import models


class CommonModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
    )  # 해당 object 생성 시간을 기준 // 업데이트 안 됨
    updated_at = models.DateTimeField(
        auto_now=True,
    )  # 해당 object가 업데이트된 시간을 기준 // 업데이트 됨

    # Meta클래스는 권한, 데이터베이스 이름, 단-복수 이름, 추상화, 순서 지정 등과 같은 모델에 대한 다양한 사항을 정의하는 데 사용됨.
    class Meta:
        abstract = True  # 해당 모델은 DB에 반영되지 않음
