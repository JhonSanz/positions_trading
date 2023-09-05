from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from position.models import Account
from position.serializers.account import AccountCreateSerializer
from position.serializers.account import AccountSerializer

class AccountViewSet(ModelViewSet):
	serializer_class = AccountSerializer
	queryset = Account.objects.all()
	permission_classes = [] # [IsAuthenticated]

	def get_serializer_class(self):
		if self.action in ["create", "update"]:
			self.serializer_class = AccountCreateSerializer
		return self.serializer_class
