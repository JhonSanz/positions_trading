from rest_framework import serializers
from position.models import Money


class MoneySerializer(serializers.ModelSerializer):
    class Meta:
        model = Money
        fields = ["id", "created_at", "updated_at", "currency"]


class MoneyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Money
        fields = ["currency"]

    def create(self, validated_data):
        return super().create({
            **validated_data,
            "user": self.context["request"].user
        })
