from order.models import Order


class CheckOrderOwnerMixin:

    def get_queryset(self, request):
        if request.user.is_staff:
            return Order.objects.filter()
        return Order.objects.all()
