from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django_tables2 import SingleTableMixin

from .models import Client
from .tables import ClientTable
# Create your views here.

import pdb

class IndexView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = 'clients.view_client'
    raise_exception = True
    # model = Client
    # table_class = ClientTable
    template_name = 'clients/index.html'
    context_object_name = 'clients'

    def get_queryset(self):
        return Client.objects.all().order_by('last_name')


class DetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
    permission_required = 'clients.view_client'
    raise_exception = True

    model = Client
    template_name = 'clients/detail.html'


class ClientCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'clients.add_client'
    raise_exception = True

    model = Client
    fields = [
        'first_name',
        'last_name',
        'customer_id',
        'company',
        'city',
        'state',
        'country',
        'cell_phone',
        'work_phone',
        'alt_phone',
        'fax',
        'email',
        'address',
        'zip',
        'poochon_rep'
    ]


class ClientUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'clients.change_client'
    raise_exception = True

    model = Client
    fields = [
        'first_name',
        'last_name',
        'customer_id',
        'company',
        'city',
        'state',
        'country',
        'cell_phone',
        'work_phone',
        'alt_phone',
        'fax',
        'email',
        'address',
        'zip',
        'poochon_rep'
    ]


class ClientDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'clients.delete_client'
    raise_exception = True

    model = Client
    success_url = reverse_lazy('clients:index')
