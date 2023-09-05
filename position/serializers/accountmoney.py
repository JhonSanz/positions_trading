from rest_framework import serializers
from position.models import Accountmoney


class AccountmoneySerializer(serializers.ModelSerializer):
	class Meta:
		model = Accountmoney
		fields = ['id', 'created_at', 'updated_at', 'quantity', 'account', 'money']


class AccountmoneyCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Accountmoney
		fields = ['id', 'created_at', 'updated_at', 'quantity', 'account', 'money']
