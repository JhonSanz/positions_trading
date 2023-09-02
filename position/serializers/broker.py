from rest_framework import serializers
from position.models import Broker


class BrokerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Broker
        fields = ["id", "name", "website"]
