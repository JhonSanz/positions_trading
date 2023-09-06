from django.db.models import Q


class FilterManager:
    """ Use this class in your get_queryset function to generate filters
    to filter a queryset given queryparams from request

    Example:
        filters = [
            {"param": "quantity_from", "condition": "quantity__gte"},
            {"param": "quantity_to", "condition": "quantity__lte"},
        ]
        result = FilterManager(filters, self.request.query_params).generate()
        self.queryset = self.queryset.filter(*result)
    """

    def __init__(self, filters: list[dict], queryparams: dict):
        self.filters = filters
        self.queryparams = queryparams
        self.result = []

    def generate(self) -> list:
        visited = []
        for key, value in self.queryparams.items():
            filter_ = list(filter(lambda x: x["param"] == key, self.filters))
            if filter_ and key not in visited:
                self.result.append(*[
                    Q(**{found["condition"]: value})
                    for found in filter_
                ])
                visited.append(key)

        return self.result
