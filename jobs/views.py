from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import JobCreateForm, JobProcedureForm

from .models import JobType, Job, Procedure, JobProcedure
# Create your views here.

class JobIndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'jobs/index.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        return Job.objects.all()


class JobDetailView(LoginRequiredMixin, generic.base.TemplateView):

    template_name = 'jobs/detail.html'

    def get_context_data(self, job_id, **kwargs):
        context = super(JobDetailView, self).get_context_data(**kwargs)
        job = Job.objects.get(pk=job_id)
        context['job'] = job

        client = job.client
        context['client'] = client

        procedures = Procedure.objects.filter(jobprocedure__job_id=job_id)
        context['procedures'] = procedures

        return context


class JobCreateView(generic.base.TemplateView, LoginRequiredMixin):
    form_class = JobCreateForm
    template_name = 'jobs/job_form.html'


    def get(self,request, **kwargs):
        form_1 = JobCreateForm()
        form_2 = JobProcedureForm()
        return render(request, self.template_name, {'form_1': form_1, 'form_2': form_2})