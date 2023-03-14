import django_filters as filters
from django.db.models import Q, Value
from django.db.models.functions import Concat
from unidecode import unidecode


class OrderFilters(filters.FilterSet):
    search = filters.CharFilter(method="search_filter")
    status = filters.CharFilter(method="status_filter")
    type_window = filters.CharFilter(method="type_window_filter")
    type_project = filters.CharFilter(method="type_project_filter")
    limit = filters.CharFilter(method="limit_filter")

    @staticmethod
    def search_filter(qs, name, value):
        qs = qs.filter(
            Q(full_name__icontains=value) |
            Q(number__icontains=value) |
            Q(number_units__icontains=value) |
            Q(addr__icontains=value) |
            Q(phone_number__icontains=value)
        ).distinct()
        return qs

    @staticmethod
    def limit_filter(qs, name, value):
        try:
            qs = qs.distinct()[:int(unidecode(value))]
        except:
            pass
        return qs

    @staticmethod
    def status_filter(qs, name, value):
        qs = qs.filter(status=value)
        return qs

    @staticmethod
    def type_window_filter(qs, name, value):
        qs = qs.filter(type_window=value)
        return qs

    @staticmethod
    def type_project_filter(qs, name, value):
        qs = qs.filter(type_project=value)
        return qs
