from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Order
from .forms import OrderForm
from quotes.views import TAX_RATE
from jobs.models import Job
from structure.models import JobStatus
# Create your views here.


class OrderIndexView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = 'orders.view_order'
    raise_exception = True
    template_name = 'orders/index.html'

    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.all()


class OrderDetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.base.TemplateView):
    permission_required = 'orders.view_order'
    raise_exception = True

    template_name = 'orders/detail.html'

    def get_context_data(self, pk, **kwargs):
        context = super(OrderDetailView, self).get_context_data(**kwargs)

        order = Order.objects.get(pk=pk)
        context['order'] = order
        context['id'] = str(order.id).zfill(5)
        context['client'] = order.client
        context['service_package'] = order.service_package

        context['services'] = order.services.all()
        context['total'] = sum((service.price for service in context['services']))
        context['discount'] = order.pre_tax_final - context['total']
        context['tax'] = order.pre_tax_final*TAX_RATE
        context['unit_final'] = order.pre_tax_final*(1+TAX_RATE)
        context['final'] = context['unit_final']*order.sample_number
        return context


class OrderCreateView(LoginRequiredMixin, PermissionRequiredMixin, generic.base.TemplateView):
    permission_required = 'orders.add_order'
    raise_exception = True

    template_name = 'quotes/quote_form.html'

    def get(self, request, **kwargs):
        form = OrderForm()

        return render(request, self.template_name, {'form': form})

    def post(self, request, **kwargs):
        form = OrderForm(request.POST)

        if form.is_valid():
            new_order = form.save()
            return HttpResponseRedirect(reverse('orders:detail', kwargs={'pk': new_order.pk}))

        else:
            # raise ValidationError({'field_name': ["error message",]})
            return HttpResponseRedirect(reverse('orders:order-create'))


class OrderUpdateView(LoginRequiredMixin, PermissionRequiredMixin, generic.base.TemplateView):
    permission_required = 'quotes.change_quote'
    raise_exception = True

    template_name = 'orders/order_form.html'

    def get(self, request, **kwargs):
        pk = kwargs['pk']
        order = get_object_or_404(Order, pk=pk)
        form = OrderForm(instance=order)

        return render(request, self.template_name, {'form': form})

    def post(self, request, **kwargs):
        pk = kwargs['pk']
        order = get_object_or_404(Order, pk=pk)
        form = OrderForm(request.POST, instance=order)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('orders:detail', kwargs={'pk': pk}))


class OrderDeleteView(LoginRequiredMixin, PermissionRequiredMixin, generic.base.TemplateView):
    permission_required = 'orders.delete_order'
    raise_exception = True

    template_name = 'jobs/job_confirm_delete.html'
    success_url = 'orders:index'

    def post(self, request, **kwargs):
        pk = kwargs['pk']
        order = get_object_or_404(Order, pk=pk)
        order.delete()

        return HttpResponseRedirect(reverse(self.success_url))


class ConvertToJobView(LoginRequiredMixin, PermissionRequiredMixin, generic.base.TemplateView):
    permission_required = ('quotes.view_order', 'jobs.add_job')
    raise_exception = True

    def get(self, request, **kwargs):
        pk = kwargs['pk']
        new_order = get_object_or_404(Order, pk=pk)
        # pdb.set_trace()
        job = Job.objects.create(

            job_name = new_order.name,
            client = new_order.client,
            date_submitted = new_order.order_date,
            job_status = JobStatus.objects.get(pk = 1),
            order = new_order,

        )
        procedures = []
        for service in new_order.services.all():
            for procedure in service.procedures.all():
                if procedure not in procedures:
                    procedures.append(procedure)

        job.procedures.add(*procedures)

        return HttpResponseRedirect(reverse('jobs:detail', kwargs={'job_id': job.pk}))