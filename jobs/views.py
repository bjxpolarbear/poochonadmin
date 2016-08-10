from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect

import pdb

from .forms import JobForm
from .models import Job


class JobIndexView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = 'jobs.view_job'
    raise_exception = True

    template_name = 'jobs/index.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        return Job.objects.all()


class JobDetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.base.TemplateView):
    permission_required = 'jobs.view_job'
    raise_exception = True

    template_name = 'jobs/detail.html'

    def get_context_data(self, job_id, **kwargs):
        context = super(JobDetailView, self).get_context_data(**kwargs)
        job = Job.objects.get(pk=job_id)
        context['job'] = job

        client = job.client
        context['client'] = client

        procedures = job.procedures.all()
        context['procedures'] = procedures

        return context


class JobCreateView(LoginRequiredMixin, PermissionRequiredMixin, generic.base.TemplateView):
    permission_required = 'jobs.add_job'
    raise_exception = True

    template_name = 'jobs/job_form.html'

    def get(self, request, **kwargs):
        form = JobForm()

        return render(request, self.template_name, {'form': form})

    def post(self, request, **kwargs):
        form = JobForm(request.POST)

        if form.is_valid():
            new_job = form.save()   # commit required since there is a many-to-many in it
            new_job.fill_procedure()
            new_job.save()
            return HttpResponseRedirect(reverse('jobs:detail', kwargs={'job_id': new_job.job_id}))

        else:

            return HttpResponseRedirect(reverse('jobs:job-create'))


class JobUpdateView(LoginRequiredMixin, PermissionRequiredMixin, generic.base.TemplateView):
    permission_required = 'jobs.change_job'
    raise_exception = True

    template_name = 'jobs/job_form.html'

    def get(self, request, **kwargs):
        job_id = kwargs['job_id']
        current_job = get_object_or_404(Job, pk=job_id)
        form = JobForm(instance=current_job)

        return render(request, self.template_name, {'form': form})

    def post(self, request, **kwargs):
        job_id = kwargs['job_id']
        job = get_object_or_404(Job, job_id=job_id)
        form = JobForm(request.POST, instance=job)

        if form.is_valid():
            updated_job = form.save()
            updated_job.fill_procedure()
            updated_job.save()

            return HttpResponseRedirect(reverse('jobs:detail', kwargs={'job_id': job_id}))


class JobDeleteView(LoginRequiredMixin, PermissionRequiredMixin, generic.base.TemplateView):
    permission_required = 'jobs.delete_job'
    raise_exception = True

    template_name = 'jobs/job_confirm_delete.html'
    success_url = 'jobs:index'

    def get(self, request, *args, **kwargs):
        job_id = kwargs['job_id']
        job = get_object_or_404(Job, job_id=job_id)
        return render(request, self.template_name, {'object': job})

    def post(self, request, **kwargs):
        job_id = kwargs['job_id']
        job = get_object_or_404(Job, job_id=job_id)
        job.delete()

        return HttpResponseRedirect(reverse(self.success_url))

