from django.db import models
from utils.abstract_model import AbstractModel
from utils.constant import BUY, SELL


class Money(AbstractModel):
    currency = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.currency}"


class Broker(AbstractModel):
    name = models.CharField(max_length=255)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Account(AbstractModel):
    name = models.CharField(max_length=255)
    leverage = models.FloatField()
    account_type = models.CharField(max_length=255)
    broker = models.ForeignKey(Broker, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name}: {self.broker.name}"


class Asset(AbstractModel):
    name = models.CharField(max_length=255)
    presition = models.IntegerField()
    swap_coeficient = models.CharField(null=True, blank=True, max_length=5)
    broker = models.ForeignKey(Broker, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name} - {self.broker.name}"

    def get_swap_coeficient(self):
        if self.swap_coeficient:
            return [day for day in self.swap_coeficient]
        return None


class Position(AbstractModel):
    ORDER_TYPES = (
        (BUY, "Buy"),
        (SELL, "Sell"),
    )
    open_date = models.DateTimeField()
    close_date = models.DateTimeField(null=True, blank=True)
    price = models.FloatField()
    volume = models.FloatField()
    leverage = models.FloatField()
    order_type = models.CharField(choices=ORDER_TYPES, max_length=10)
    asset = models.ForeignKey(Asset, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.asset.name} - {self.volume} - {self.price}"


class AccountMoney(AbstractModel):
    quantity = models.FloatField()
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    money = models.ForeignKey(Money, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.account.name}: {self.money.currency}"
