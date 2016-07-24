# from django.shortcuts import render
# from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Client
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'clients/index.html'
    context_object_name = 'clients'

    def get_queryset(self):
        return Client.objects.all()


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Client
    template_name = 'clients/detail.html'


class ClientCreate(LoginRequiredMixin, CreateView):
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


class ClientUpdate(LoginRequiredMixin, UpdateView):
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


class ClientDelete(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('clients:index')