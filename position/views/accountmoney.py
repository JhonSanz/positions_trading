from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from position.models import AccountMoney
from position.serializers.accountmoney import AccountMoneyCreateSerializer
from position.serializers.accountmoney import AccountMoneySerializer
from utils.filter_with_params import FilterManager
from utils.paginator import CustomPagination

class AccountMoneyViewSet(ModelViewSet):
	serializer_class = AccountMoneySerializer
	queryset = AccountMoney.objects
	permission_classes = [IsAuthenticated]
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
			]
			result = FilterManager(filters, self.request.query_params).generate()
			self.queryset = self.queryset.filter(*result)
		return self.queryset
