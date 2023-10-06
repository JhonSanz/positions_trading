from rest_framework import serializers
from position.models import Account
from position.serializers.accountmoney import AccountMoneyTotalSerializer


class AccountMiniSerializer(serializers.ModelSerializer):
    deposits = AccountMoneyTotalSerializer(source='get_total_money', many=True)

    class Meta:
        model = Account
        fields = ['id', 'name', 'deposits']


class AccountSerializer(serializers.ModelSerializer):
    deposits = AccountMoneyTotalSerializer(source='get_total_money', many=True)
    broker = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = [
            'id', 'created_at', 'updated_at', 'name',
            'leverage', 'account_type', 'broker', 'deposits'
        ]

    def get_broker(self, obj):
        return {
            "name": obj.broker.name,
            "id": obj.broker.id
        }


class AccountCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['name', 'leverage', 'account_type', 'broker']
