from django.contrib import admin
from position.models import Money, Broker, Account, Asset, Position

# Register your models here.
admin.site.register(Money)
admin.site.register(Broker)
admin.site.register(Account)
admin.site.register(Asset)
admin.site.register(Position)
