import django_filters as filters
from django.db.models import Q, Value
from django.db.models.functions import Concat
from unidecode import unidecode


class UserFilters(filters.FilterSet):
    search = filters.CharFilter(method="search_filter")
    status = filters.CharFilter(method="status_filter")
    admin = filters.CharFilter(method="admin_filter")
    limit = filters.CharFilter(method="limit_filter")

    @staticmethod
    def search_filter(qs, name, value):
        qs = qs.filter(
            Q(email__icontains=value) |
            Q(phone_number__icontains=value) |
            Q(full_name__icontains=value)
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
        if value == '1':
            qs = qs.filter(is_active=1)
        else:
            qs = qs.filter(is_active=0)
        return qs

    @staticmethod
    def admin_filter(qs, name, value):
        if value == '1':
            qs = qs.filter(is_admin=1)
        else:
            qs = qs.filter(is_admin=0)
        return qs
