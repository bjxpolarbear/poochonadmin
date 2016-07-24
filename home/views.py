from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class HomePageView(LoginRequiredMixin, generic.TemplateView):
    login_url = 'users:login'
    redirect_field_name = 'redirect_to'
    template_name = 'home/index.html'
