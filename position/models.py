from django.db import models
from utilities.models import AbstractModel
from utilities.constant import PositionsType, DirectionType


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
    swap_coeficient = models.CharField(
        null=True, blank=True, max_length=7,
        default="0"*7
    )
    long_swap_coeficient = models.FloatField(default=0)
    short_swap_coeficient = models.FloatField(default=0)
    account = models.ForeignKey(Account, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name} - {self.account.name}"

    def get_swap_coeficient(self):
        if self.swap_coeficient:
            return [int(day) for day in self.swap_coeficient]
        return []


class Position(AbstractModel):
    ORDER_TYPES = (
        (PositionsType.LONG, "Long"),
        (PositionsType.SHORT, "Short"),
    )
    DIRECTION_TYPES = (
        (DirectionType.IN, "In"),
        (DirectionType.OUT, "Out"),
    )
    reference = models.ForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)    
    open_date = models.DateTimeField()
    close_date = models.DateTimeField(null=True, blank=True)
    price = models.FloatField()
    volume = models.FloatField()
    is_leveraged = models.BooleanField(default=False)
    order_type = models.SmallIntegerField(choices=ORDER_TYPES)
    direction = models.SmallIntegerField(choices=DIRECTION_TYPES, default=DirectionType.IN)
    asset = models.ForeignKey(Asset, on_delete=models.PROTECT)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.asset.name} - {self.volume} - {self.price}"


class AccountMoney(AbstractModel):
    quantity = models.FloatField()
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    money = models.ForeignKey(Money, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.account.name}: {self.money.currency}"
