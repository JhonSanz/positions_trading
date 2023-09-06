from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from position.models import Asset
from position.serializers.asset import AssetCreateSerializer
from position.serializers.asset import AssetSerializer
from utils.filter_with_params import FilterManager


class AssetViewSet(ModelViewSet):
	serializer_class = AssetSerializer
	queryset = Asset.objects.all()
	permission_classes = [] # [IsAuthenticated]

	def get_serializer_class(self):
		if self.action in ["create", "update"]:
			self.serializer_class = AssetCreateSerializer
		return self.serializer_class

	def get_queryset(self):
		if self.action in ["list"]:
			filters = [
				{"param": "name", "condition": "name__icontains"},
			]
			result = FilterManager(filters, self.request.query_params).generate()
			self.queryset = self.queryset.filter(*result)
		return self.queryset
