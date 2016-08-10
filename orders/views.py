from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic

from .models import Order
# Create your views here.


class OrderIndexView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = 'orders.view_order'
    raise_exception = True
    template_name = 'orders/index.html'

    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.all()