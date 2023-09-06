from rest_framework import serializers
from position.models import Asset


class AssetSerializer(serializers.ModelSerializer):
	swap_coeficient = serializers.ListField(source="get_swap_coeficient")
	class Meta:
		model = Asset
		fields = [
			'id', 'created_at', 'updated_at', 'name',
			'presition', 'swap_coeficient', 'account',
			'long_swap_coeficient', 'short_swap_coeficient'
		]


class AssetCreateSerializer(serializers.ModelSerializer):
	swap_coeficient = serializers.RegexField("^\d{7}$")
	class Meta:
		model = Asset
		fields = [
			'name', 'presition', 'swap_coeficient', 'account',
			'long_swap_coeficient', 'short_swap_coeficient'
		]
