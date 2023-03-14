import django_filters as filters
from django.db.models import Q, Value
from django.db.models.functions import Concat
from unidecode import unidecode


class ClassFilters(filters.FilterSet):
    search = filters.CharFilter(method="search_filter")
    status = filters.CharFilter(method="status_filter")
    category = filters.CharFilter(method="category_filter")
    is_show_in_slider = filters.CharFilter(method="is_show_in_slider_filter")
    limit = filters.CharFilter(method="limit_filter")

    @staticmethod
    def search_filter(qs, name, value):
        qs = qs.filter(
            Q(teacher__user__first_name__icontains=value) |
            Q(teacher__user__last_name__icontains=value) |
            Q(teacher__user__national_id__icontains=value) |
            Q(teacher__user__father_name__icontains=value) |
            Q(teacher__user__phone__icontains=value) |
            Q(title__icontains=value) |
            Q(desc__icontains=value) |
            Q(users_limit__icontains=value) |
            Q(amount__icontains=value)
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
    def category_filter(qs, name, value):
        qs = qs.filter(category=value)
        return qs

    @staticmethod
    def is_show_in_slider_filter(qs, name, value):
        qs = qs.filter(is_show_in_slider=value)
        return qs


class ClassUserFilters(filters.FilterSet):
    search = filters.CharFilter(method="search_filter")
    status = filters.CharFilter(method="status_filter")
    limit = filters.CharFilter(method="limit_filter")

    @staticmethod
    def search_filter(qs, name, value):
        qs = qs.filter(
            Q(class_item__teacher__user__first_name__icontains=value) |
            Q(class_item__teacher__user__last_name__icontains=value) |
            Q(class_item__teacher__user__national_id__icontains=value) |
            Q(class_item__teacher__user__father_name__icontains=value) |
            Q(class_item__teacher__user__phone__icontains=value) |
            Q(user__first_name__icontains=value) |
            Q(user__last_name__icontains=value) |
            Q(user__national_id__icontains=value) |
            Q(user__father_name__icontains=value) |
            Q(user__phone__icontains=value)
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


class CategoryFilters(filters.FilterSet):
    search = filters.CharFilter(method="search_filter")
    limit = filters.CharFilter(method="limit_filter")

    @staticmethod
    def search_filter(qs, name, value):
        qs = qs.filter(
            Q(title__icontains=value)
        ).distinct()
        return qs

    @staticmethod
    def limit_filter(qs, name, value):
        try:
            qs = qs.distinct()[:int(unidecode(value))]
        except:
            pass
        return qs
