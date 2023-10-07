from django.db import transaction
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from position.models import Broker, Account, Asset, Position, AccountMoney
from position.serializers.broker import BrokerCreateSerializer
from position.serializers.broker import BrokerSerializer
from utilities.filter_with_params import FilterManager
from utilities.paginator import CustomPagination


class BrokerViewSet(ModelViewSet):
	serializer_class = BrokerSerializer
	queryset = Broker.objects
	permission_classes = [IsAuthenticated]
	pagination_class = CustomPagination

	def get_serializer_class(self):
		if self.action in ["create", "update"]:
			self.serializer_class = BrokerCreateSerializer
		return self.serializer_class

	def get_queryset(self):
		if self.action in ["list"]:
			filters = [
				{"param": "name", "condition": "name__icontains"},
			]
			result = FilterManager(filters, self.request.query_params).generate()
			self.queryset = self.queryset.filter(user=self.request.user, *result)
		return self.queryset

	@transaction.atomic
	def destroy(self, request, pk):
		broker = self.get_object()
		Position.objects.filter(asset__account__broker=broker).delete()
		AccountMoney.objects.filter(account__broker=broker).delete()
		Asset.objects.filter(account__broker=broker).delete()
		Account.objects.filter(broker=broker).delete()
		return super().destroy(request)
