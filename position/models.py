from django.db import models
from utilities.models import AbstractModel
from utilities.constant import LONG, SHORT, IN, OUT


class Money(AbstractModel):
    # user = models.ForeignKey("utilities.CustomUser", on_delete=models.PROTECT)
    currency = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.currency}"


class Broker(AbstractModel):
    name = models.CharField(max_length=255)
    website = models.URLField(null=True, blank=True)
    user = models.ForeignKey("utilities.CustomUser", on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def get_accounts(self):
        return self.account_set.all()


class Account(AbstractModel):
    name = models.CharField(max_length=255)
    details = models.TextField(null=True, blank=True)
    leverage = models.FloatField()
    account_type = models.CharField(max_length=255)
    broker = models.ForeignKey(Broker, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name}: {self.broker.name}"

    def get_total_money(self):
        return (
            self.accountmoney_set.values("money__currency")
            .annotate(total=models.Sum('quantity'))
        )


class Asset(AbstractModel):
    name = models.CharField(max_length=255)
    presition = models.IntegerField()
    lot = models.PositiveIntegerField()
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

    def get_swap_coeficient_display(self):
        if self.swap_coeficient:
            return ",".join(self.swap_coeficient)
        return ""


class Position(AbstractModel):
    ORDER_TYPES = (
        (LONG, "Long"),
        (SHORT, "Short"),
    )
    DIRECTION_TYPES = (
        (IN, "In"),
        (OUT, "Out"),
    )
    reference = models.ForeignKey(
        "self", on_delete=models.PROTECT, null=True, blank=True)
    open_date = models.DateTimeField()
    close_date = models.DateTimeField(null=True, blank=True, default=None)
    price = models.FloatField()
    volume = models.FloatField()
    is_leveraged = models.BooleanField(default=False)
    order_type = models.CharField(
        choices=ORDER_TYPES, max_length=2
    )
    direction = models.CharField(
        max_length=2,
        choices=DIRECTION_TYPES, default=IN
    )
    asset = models.ForeignKey(Asset, on_delete=models.PROTECT)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.asset.name} - {self.volume} - {self.price}"

    def get_sub_positions(self):
        return Position.objects.filter(reference=self)


class AccountMoney(AbstractModel):
    quantity = models.FloatField()
    date_deposit = models.DateTimeField(null=True, blank=True, default=None)
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    money = models.ForeignKey(Money, on_delete=models.PROTECT)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.account.name}: {self.money.currency}"
