from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from position.models import Position
from position.serializers.position import PositionCreateSerializer
from position.serializers.position import PositionSerializer

class PositionViewSet(ModelViewSet):
	serializer_class = PositionSerializer
	queryset = Position.objects.all()
	permission_classes = [] # [IsAuthenticated]

	def get_serializer_class(self):
		if self.action in ["create", "update"]:
			self.serializer_class = PositionCreateSerializer
		return self.serializer_class
