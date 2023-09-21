from rest_framework import serializers
from position.models import Broker
from position.serializers.account import AccountMiniSerializer


class BrokerSerializer(serializers.ModelSerializer):
    accounts = AccountMiniSerializer(source="get_accounts", many=True)
    class Meta:
        model = Broker
        fields = [
            'id', 'created_at', 'updated_at', 'name', 'website',
            'accounts'
        ]


class BrokerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Broker
        fields = ['name', 'website']
