from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from position.models import Position
from position.serializers.position import PositionCreateSerializer
from position.serializers.position import PositionSerializer
from utils.filter_with_params import FilterManager
from utils.paginator import CustomPagination


class PositionViewSet(ModelViewSet):
	serializer_class = PositionSerializer
	queryset = Position.objects.all()
	permission_classes = [IsAuthenticated]
	pagination_class = CustomPagination

	def get_serializer_class(self):
		if self.action in ["create", "update"]:
			self.serializer_class = PositionCreateSerializer
		return self.serializer_class

	def get_queryset(self):
		if self.action in ["list"]:
			filters = [
				{"param": "price", "condition": "price"},
				{"param": "price_from", "condition": "price__gte"},
				{"param": "price_to", "condition": "price__lte"},
				{"param": "order_type", "condition": "order_type"},
				{"param": "open_date_from", "condition": "open_date__gte"},
				{"param": "open_date_to", "condition": "open_date__lte"},
				{"param": "close_date_from", "condition": "close_date__gte"},
				{"param": "close_date_to", "condition": "close_date__lte"},
			]
			result = FilterManager(filters, self.request.query_params).generate()
			self.queryset = self.queryset.filter(*result)
		return self.queryset
