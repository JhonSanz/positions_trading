from django.db import transaction
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from position.models import Account, Asset, Position, AccountMoney
from position.serializers.account import AccountCreateSerializer
from position.serializers.account import AccountSerializer
from utilities.filter_with_params import FilterManager
from utilities.paginator import CustomPagination


class AccountViewSet(ModelViewSet):
	serializer_class = AccountSerializer
	queryset = Account.objects
	permission_classes = [IsAuthenticated]
	pagination_class = CustomPagination

	def get_serializer_class(self):
		if self.action in ["create", "update"]:
			self.serializer_class = AccountCreateSerializer
		return self.serializer_class

	def get_queryset(self):
		if self.action in ["list"]:
			filters = [
				{"param": "name", "condition": "name__icontains"},
				{"param": "broker", "condition": "broker"},
			]
			result = FilterManager(filters, self.request.query_params).generate()
			self.queryset = self.queryset.filter(*result)
		return self.queryset

	@transaction.atomic
	def destroy(self, request, pk):
		account = self.get_object()
		Position.objects.filter(asset__account=account).delete()
		AccountMoney.objects.filter(account=account).delete()
		Asset.objects.filter(account=account).delete()
		return super().destroy(request)
