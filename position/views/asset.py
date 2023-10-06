from django.db import transaction
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from position.models import Asset, Position, AccountMoney
from position.serializers.asset import AssetCreateSerializer
from position.serializers.asset import AssetSerializer
from utilities.filter_with_params import FilterManager
from utilities.paginator import CustomPagination


class AssetViewSet(ModelViewSet):
	serializer_class = AssetSerializer
	queryset = Asset.objects
	permission_classes = []#[IsAuthenticated]
	pagination_class = CustomPagination

	def get_serializer_class(self):
		if self.action in ["create", "update"]:
			self.serializer_class = AssetCreateSerializer
		return self.serializer_class

	def get_queryset(self):
		if self.action in ["list"]:
			filters = [
				{"param": "name", "condition": "name__icontains"},
				{"param": "account", "condition": "account__id"},
			]
			result = FilterManager(filters, self.request.query_params).generate()
			self.queryset = self.queryset.filter(*result)
		return self.queryset

	@transaction.atomic
	def destroy(self, request, pk):
		Position.objects.filter(asset=self.get_object()).delete()
		return super().destroy(request)
