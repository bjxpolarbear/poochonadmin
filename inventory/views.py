from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Item
from .forms import ItemForm

# Create your views here.
class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'inventory/index.html'
    context_object_name = 'items'

    def get_queryset(self):
        return Item.objects.all().order_by('-date_received')


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Item
    template_name = 'inventory/detail.html'


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Item
    form_class = ItemForm

    # fields = [
    #     'name',
    #     'item_id',
    #     'category',
    #     'unit',
    #     'quantity',
    #     'unit_price',
    #     'date_received',
    #     'location',
    #     'sub_location',
    #     'description',
    # ]


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    form_class = ItemForm

    # fields = [
    #     'name',
    #     'item_id',
    #     'category',
    #     'unit',
    #     'quantity',
    #     'unit_price',
    #     'date_received',
    #     'location',
    #     'sub_location',
    #     'description',
    # ]


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = reverse_lazy('inventory:index')
