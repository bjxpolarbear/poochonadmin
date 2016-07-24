from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from .models import Quote, QuoteProcedure

# Create your views here.
class QuoteIndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'quotes/index.html'
    context_object_name = 'quotes'

    def get_queryset(self):
        return Quote.objects.all()