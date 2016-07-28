from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.forms.models import model_to_dict

from .models import Quote, QuoteProcedure, Sample
from structure.models import Procedure
from .forms import QuoteForm, SampleForm, QuoteProcedureForm
from jobs.views import fill_procedure



# Create your views here.
class QuoteIndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'quotes/index.html'
    context_object_name = 'quotes'

    def get_queryset(self):
        return Quote.objects.all()


class QuoteDetailView(LoginRequiredMixin, generic.base.TemplateView):

    template_name = 'quotes/detail.html'

    def get_context_data(self, pk, **kwargs):
        context = super(QuoteDetailView, self).get_context_data(**kwargs)
        quote = Quote.objects.get(pk=pk)
        context['quote'] = quote

        client = quote.client
        context['client'] = client

        procedures = Procedure.objects.filter(quoteprocedure__quote_id=pk)
        context['procedures'] = procedures

        return context


class QuoteCreateView(LoginRequiredMixin, generic.base.TemplateView):
    template_name = 'jobs/job_form.html'

    def get(self,request, **kwargs):
        form_1 = QuoteForm()
        form_2 = QuoteProcedureForm()
        return render(request, self.template_name, {'form_1': form_1, 'form_2': form_2})

    def post(self, request, **kwargs):
        form_1 = QuoteForm(request.POST)
        form_2 = QuoteProcedureForm(request.POST)

        if form_1.is_valid() and form_2.is_valid():
            new_quote = form_1.save()
            procedures_pk = request.POST.getlist('procedure')
            procedures_pk = fill_procedure(procedures_pk)

            for procedure_pk in procedures_pk:
                QuoteProcedure.objects.create(quote=new_quote, procedure=Procedure.objects.get(pk=procedure_pk))

            return HttpResponseRedirect(reverse('quotes:index'))

        else:

            return HttpResponseRedirect(reverse('quotes:quote-create'))

class QuoteUpdateView(generic.base.TemplateView, LoginRequiredMixin):
    template_name = 'jobs/job_form.html'

    def get(self, request, pk, **kwargs):
        instance = Quote.objects.get(pk=pk)
        data_1 = model_to_dict(instance)
        data_2 = [quoteprocedure.procedure.procedure_id for quoteprocedure in QuoteProcedure.objects.filter(quote=instance)]

        form_1 = QuoteForm(initial=data_1)
        form_2 = QuoteProcedureForm(initial={'procedure': data_2})

        return render(request, self.template_name, {'form_1': form_1, 'form_2': form_2})

    def post(self, request, pk, **kwargs):
        instance = get_object_or_404(Quote, pk=pk)
        form_1 = QuoteForm(request.POST, instance=instance)
        form_2 = QuoteProcedureForm(request.POST)

        if form_1.is_valid() and form_2.is_valid():
            form_1.save()
            procedures_pk = request.POST.getlist('procedure')
            procedures_pk = fill_procedure(procedures_pk)
            procedures = Procedure.objects.filter(procedure_id__in=procedures_pk)

            # load the old procedure list
            old_procedures = Procedure.objects.filter(quoteprocedure__quote_id=pk)

            # Find the procedures in old list but not in new list
            for_delete = set(old_procedures).difference(set(procedures))

            QuoteProcedure.objects.filter(procedure__in=for_delete).delete()
            # pdb.set_trace()
            for procedure_pk in procedures_pk:
                QuoteProcedure.objects.get_or_create(quote=Quote.objects.get(pk=pk),procedure=Procedure.objects.get(procedure_id=procedure_pk))


            return HttpResponseRedirect(reverse('jobs:index'))


class QuoteDeleteView(generic.base.TemplateView, LoginRequiredMixin):
    template_name = 'jobs/job_confirm_delete.html'
    success_url = 'quotes:index'

    def post(self, request, pk, **kwargs):
        instance = get_object_or_404(Quote, pk=pk)
        instance.delete()
        job_procedures = QuoteProcedure.objects.filter(quote_id=pk)
        for job_procedure in job_procedures:
            job_procedure.delete()

        return HttpResponseRedirect(reverse(self.success_url))