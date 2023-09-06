from rest_framework import serializers
from position.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'id', 'created_at', 'updated_at', 'name',
            'leverage', 'account_type', 'broker'
        ]


class AccountCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['name', 'leverage', 'account_type', 'broker']
