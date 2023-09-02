from rest_framework.viewsets import ModelViewSet
from position.models import Broker
from position.serializers.broker import BrokerSerializer


class BrokerViewSet(ModelViewSet):
    serializer_class = BrokerSerializer
    queryset = Broker.objects.all()
