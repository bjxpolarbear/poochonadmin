from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Item
from .forms import ItemForm

# Create your views here.
class IndexView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = 'inventory.view_item'
    raise_exception = True

    template_name = 'inventory/index.html'
    context_object_name = 'items'

    def get_queryset(self):
        return Item.objects.all().order_by('-date_received')


class ItemDetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
    permission_required = 'inventory.view_item'
    raise_exception = True

    model = Item
    template_name = 'inventory/detail.html'


class ItemCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'inventory.add_item'
    raise_exception = True

    model = Item
    form_class = ItemForm


class ItemUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'inventory.change_item'
    raise_exception = True

    model = Item
    form_class = ItemForm


class ItemDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'inventory.delete_item'
    raise_exception = True

    model = Item
    success_url = reverse_lazy('inventory:index')
