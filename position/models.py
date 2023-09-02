from django.db import models
from utils.abstract_model import AbstractModel


class Broker(AbstractModel):
    name = models.CharField(max_length=255)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Position(AbstractModel):
    open_date = models.DateTimeField()
    close_date = models.DateTimeField(null=True, blank=True)
    price = models.FloatField()
    volume = models.FloatField()
    leverage = models.FloatField()
    broker = models.ForeignKey(Broker, on_delete=models.PROTECT)
    asset = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.asset} - {self.volume} - {self.price}"
