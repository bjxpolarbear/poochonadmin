from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import JobType, Job, Procedure, JobProcedure
# Create your views here.

class JobIndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'jobs/index.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        return Job.objects.all()
