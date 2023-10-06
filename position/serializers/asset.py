from rest_framework import serializers
from position.models import Asset


class AssetSerializerMini(serializers.ModelSerializer):
	class Meta:
		model = Asset
		fields = ['id', 'name']


class AssetSerializer(serializers.ModelSerializer):
	# swap_coeficient = serializers.ListField(source="get_swap_coeficient_display")
	account = serializers.SerializerMethodField()
	class Meta:
		model = Asset
		fields = [
			'id', 'created_at', 'updated_at', 'name',
			'presition', 'swap_coeficient', 'account',
			'long_swap_coeficient', 'short_swap_coeficient'
		]

	def get_account(self, obj):
		return {
			"name": obj.account.name,
            "id": obj.account.id
		}


class AssetCreateSerializer(serializers.ModelSerializer):
	swap_coeficient = serializers.RegexField("^\d{7}$")
	class Meta:
		model = Asset
		fields = [
			'name', 'presition', 'swap_coeficient', 'account',
			'long_swap_coeficient', 'short_swap_coeficient'
		]
