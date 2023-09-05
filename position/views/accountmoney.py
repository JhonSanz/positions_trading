from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from position.models import Accountmoney
from position.serializers.accountmoney import AccountmoneyCreateSerializer
from position.serializers.accountmoney import AccountmoneySerializer

class AccountmoneyViewSet(ModelViewSet):
	serializer_class = AccountmoneySerializer
	queryset = Accountmoney.objects.all()
	permission_classes = [] # [IsAuthenticated]

	def get_serializer_class(self):
		if self.action in ["create", "update"]:
			self.serializer_class = AccountmoneyCreateSerializer
		return self.serializer_class
