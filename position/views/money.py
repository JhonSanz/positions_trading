from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from position.models import Money
from position.serializers.money import MoneyCreateSerializer
from position.serializers.money import MoneySerializer

class MoneyViewSet(ModelViewSet):
	serializer_class = MoneySerializer
	queryset = Money.objects.all()
	permission_classes = [] # [IsAuthenticated]

	def get_serializer_class(self):
		if self.action in ["create", "update"]:
			self.serializer_class = MoneyCreateSerializer
		return self.serializer_class
