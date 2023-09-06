from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from position.models import AccountMoney
from position.serializers.accountmoney import AccountMoneyCreateSerializer
from position.serializers.accountmoney import AccountMoneySerializer


class AccountMoneyViewSet(ModelViewSet):
	serializer_class = AccountMoneySerializer
	queryset = AccountMoney.objects.all()
	permission_classes = [] # [IsAuthenticated]

	def get_serializer_class(self):
		if self.action in ["create", "update"]:
			self.serializer_class = AccountMoneyCreateSerializer
		return self.serializer_class
