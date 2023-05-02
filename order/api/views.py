from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from order.api.serializers import *
from order.models import Order
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = []

        return super().get_permissions()
