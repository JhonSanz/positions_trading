from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from position.models import Position


class Filters(ViewSet):
    def list(self, request):
        filters = Position.objects.filter(
            # asset__account__broker__user=request.user
        ).order_by().values("asset__id", "asset__name").distinct()
        print(filters.query)
        return Response(filters)
