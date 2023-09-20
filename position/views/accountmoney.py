from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from position.models import AccountMoney
from position.serializers.accountmoney import AccountMoneyCreateSerializer
from position.serializers.accountmoney import AccountMoneySerializer
from utilities.filter_with_params import FilterManager
from utilities.paginator import CustomPagination

class AccountMoneyViewSet(ModelViewSet):
	serializer_class = AccountMoneySerializer
	queryset = AccountMoney.objects
	permission_classes = []#[IsAuthenticated]
	pagination_class = CustomPagination

	def get_serializer_class(self):
		if self.action in ["create", "update"]:
			self.serializer_class = AccountMoneyCreateSerializer
		return self.serializer_class

	def get_queryset(self):
		if self.action in ["list"]:
			filters = [
				{"param": "quantity_from", "condition": "quantity__gte"},
				{"param": "quantity_to", "condition": "quantity__lte"},
				{"param": "created_at_from", "condition": "created_at__date__gte"},
				{"param": "created_at_to", "condition": "created_at__date__lte"},
				{"param": "account", "condition": "account__id"},
			]
			result = FilterManager(filters, self.request.query_params).generate()
			self.queryset = self.queryset.filter(*result)
		return self.queryset
