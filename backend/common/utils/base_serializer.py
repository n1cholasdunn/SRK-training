from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField


class BaseOwnerFieldSerializer(ModelSerializer):
    trainee = PrimaryKeyRelatedField(read_only=True)

    def save(self, **kwargs):
        kwargs["trainee"] = self.context["request"].user
        return super().save(**kwargs)

    class Meta:
        abstract = True
