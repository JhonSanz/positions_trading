from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from position.models import Money
from position.serializers.money import MoneyCreateSerializer
from position.serializers.money import MoneySerializer
from utilities.filter_with_params import FilterManager
from utilities.paginator import CustomPagination


class MoneyViewSet(ModelViewSet):
	serializer_class = MoneySerializer
	queryset = Money.objects
	permission_classes = [IsAuthenticated]
	pagination_class = CustomPagination

	def get_serializer_class(self):
		if self.action in ["create", "update"]:
			self.serializer_class = MoneyCreateSerializer
		return self.serializer_class

	def get_queryset(self):
		if self.action in ["list"]:
			filters = [
				{"param": "currency", "condition": "currency__icontains"},
			]
			result = FilterManager(filters, self.request.query_params).generate()
			self.queryset = self.queryset.filter(*result)
		return self.queryset
