from rest_framework import serializers
from position.models import AccountMoney
from position.serializers.money import MoneySerializer


class AccountMoneyTotalSerializer(serializers.Serializer):
    money__currency = serializers.CharField()
    total = serializers.FloatField()


class AccountMoneySerializer(serializers.ModelSerializer):
    money = MoneySerializer()
    date_deposit = serializers.DateTimeField(format="%Y-%m-%d %H:%M")

    class Meta:
        model = AccountMoney
        fields = [
            'id', 'created_at', 'updated_at', 'quantity',
            'account', 'money', 'description', 'date_deposit'
        ]


class AccountMoneyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountMoney
        fields = ['quantity', 'date_deposit', 'account', 'money', 'description']
