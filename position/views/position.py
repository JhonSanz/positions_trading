from rest_framework.viewsets import ModelViewSet
from position.models import Position
from position.serializers.position import PositionSerializer


class PositionViewSet(ModelViewSet):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()
