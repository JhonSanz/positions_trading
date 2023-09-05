from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from position.models import Broker
from position.serializers.broker import BrokerCreateSerializer
from position.serializers.broker import BrokerSerializer

class BrokerViewSet(ModelViewSet):
	serializer_class = BrokerSerializer
	queryset = Broker.objects.all()
	permission_classes = [] # [IsAuthenticated]

	def get_serializer_class(self):
		if self.action in ["create", "update"]:
			self.serializer_class = BrokerCreateSerializer
		return self.serializer_class
