from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.forms.models import model_to_dict
import pdb

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
    template_name = 'jobs/job_form.html'

    def get(self,request, **kwargs):
        form_1 = JobCreateForm()
        form_2 = JobProcedureForm()
        return render(request, self.template_name, {'form_1': form_1, 'form_2': form_2})

    def post(self,request, **kwargs):
        form_1 = JobCreateForm(request.POST)
        form_2 = JobProcedureForm(request.POST)

        if form_1.is_valid() and form_2.is_valid():
            new_job = form_1.save()
            procedures_pk = request.POST.getlist('procedure')
            procedures_pk = fill_procedure(procedures_pk)

            for procedure_pk in procedures_pk:
                JobProcedure.objects.create(job=new_job, procedure=Procedure.objects.get(pk=procedure_pk))

            return HttpResponseRedirect('/jobs/')

        else:

            return HttpResponseRedirect('/jobs/add')


class JobUpdateView(generic.base.TemplateView, LoginRequiredMixin):
    template_name = 'jobs/job_form.html'

    def get(self, request, job_id, **kwargs):
        current_job = Job.objects.get(pk=job_id)
        data_1 = model_to_dict(current_job)
        data_2 = [jobprocedure.procedure.procedure_id for jobprocedure in JobProcedure.objects.filter(job_id=job_id)]

        form_1 = JobCreateForm(initial=data_1)
        form_2 = JobProcedureForm(initial={'procedure': data_2})

        return render(request, self.template_name, {'form_1': form_1, 'form_2': form_2})

    def post(self, request, job_id, **kwargs):
        instance = get_object_or_404(Job, job_id=job_id)
        form_1 = JobCreateForm(request.POST, instance=instance)
        form_2 = JobProcedureForm(request.POST)

        if form_1.is_valid() and form_2.is_valid():
            form_1.save()
            procedures_pk = request.POST.getlist('procedure')
            procedures_pk = fill_procedure(procedures_pk)
            procedures = Procedure.objects.filter(procedure_id__in=procedures_pk)
            old_procedures = Procedure.objects.filter(jobprocedure__job__job_id=job_id)


            for_delete = set(old_procedures).difference(set(procedures))  #Find the procedures in old list but not in new list

            JobProcedure.objects.filter(procedure__in=for_delete).delete()
            # pdb.set_trace()
            for procedure_pk in procedures_pk:
                JobProcedure.objects.get_or_create(job=Job.objects.get(job_id=job_id),procedure=Procedure.objects.get(procedure_id=procedure_pk))




            return HttpResponseRedirect('/jobs/')


def fill_procedure(procedures_pk):
    # filling the ancestors
    for procedure_pk in procedures_pk:
        ancestors = Procedure.objects.get(pk=procedure_pk).get_ancestors()
        for ancestor in ancestors:
            if str(ancestor.pk) not in procedures_pk:
                procedures_pk.append(str(ancestor.pk))

    return procedures_pk