from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from position.models import Broker
from position.serializers.broker import BrokerCreateSerializer
from position.serializers.broker import BrokerSerializer
from utils.filter_with_params import FilterManager

class BrokerViewSet(ModelViewSet):
	serializer_class = BrokerSerializer
	queryset = Broker.objects.all()
	permission_classes = [] # [IsAuthenticated]

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
			self.queryset = self.queryset.filter(*result)
		return self.queryset
