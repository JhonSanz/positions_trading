from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from position.models import Position
from position.serializers.position import PositionCreateSerializer
from position.serializers.position import PositionSerializer
from utilities.filter_with_params import FilterManager
from utilities.paginator import CustomPagination


class PositionViewSet(ModelViewSet):
	serializer_class = PositionSerializer
	queryset = Position.objects
	permission_classes = []#[IsAuthenticated]
	pagination_class = CustomPagination

	def get_serializer_class(self):
		if self.action in ["create", "update"]:
			self.serializer_class = PositionCreateSerializer
		return self.serializer_class

	def get_queryset(self):
		if self.action in ["list"]:
			filters = [
				{"param": "price", "condition": "price"},
				{"param": "volume", "condition": "volume"},
				{"param": "price_from", "condition": "price__gte"},
				{"param": "price_to", "condition": "price__lte"},
				{"param": "order_type", "condition": "order_type"},
				{"param": "direction", "condition": "direction"},
				{"param": "open_date_from", "condition": "open_date__date__gte"},
				{"param": "open_date_to", "condition": "open_date__date__lte"},
				{"param": "close_date_from", "condition": "close_date__date__gte"},
				{"param": "close_date_to", "condition": "close_date__date__lte"},
				{"param": "account", "condition": "asset__account__id"},
				{"param": "asset", "condition": "asset__id"},
				{"param": "reference", "condition": "reference__isnull"},
			]
			result = FilterManager(filters, self.request.query_params).generate()
			self.queryset = self.queryset.filter(*result)
		return self.queryset

	@action(detail=True, methods=["GET"])
	def sub_positions(self, request, pk=None):
		position = self.get_object()
		self.queryset = position.get_sub_positions()
		return super().list(request, pk=None)

	def destroy(self, request, pk):
		position = self.get_object()
		Position.objects.filter(reference=position.id).delete()
		return super().destroy(request)
