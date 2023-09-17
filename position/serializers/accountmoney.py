from rest_framework import serializers
from position.models import AccountMoney
from position.serializers.money import MoneySerializer


class AccountMoneyTotalSerializer(serializers.Serializer):
    money__currency = serializers.CharField()
    total = serializers.FloatField()


class AccountMoneySerializer(serializers.ModelSerializer):
    money = MoneySerializer()

    class Meta:
        model = AccountMoney
        fields = [
            'id', 'created_at', 'updated_at', 'quantity',
            'account', 'money'
        ]


class AccountMoneyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountMoney
        fields = ['quantity', 'account', 'money']
