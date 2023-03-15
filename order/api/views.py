from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from order.api.serializers import *
from order.models import Order
from rest_framework.permissions import IsAdminUser


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
