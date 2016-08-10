from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


from .models import Quote
from .forms import QuoteForm
from orders.models import Order
from structure.models import OrderStatus
import pdb


TAX_RATE = 0.07

# Create your views here.
class QuoteIndexView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = 'quotes.view_quote'
    raise_exception = True

    template_name = 'quotes/index.html'
    context_object_name = 'quotes'

    def get_queryset(self):
        return Quote.objects.all()


class QuoteDetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.base.TemplateView):
    permission_required = 'quotes.view_quote'
    raise_exception = True

    template_name = 'quotes/detail.html'

    def get_context_data(self, pk, **kwargs):
        context = super(QuoteDetailView, self).get_context_data(**kwargs)
        quote = Quote.objects.get(pk=pk)
        context['quote'] = quote
        context['quote_id'] = str(quote.id).zfill(5)
        client = quote.client
        context['client'] = client
        context['service_package'] = quote.service_package

        context['services'] = quote.services.all()
        context['total'] = sum((service.price for service in context['services']))
        context['discount'] = quote.pre_tax_final - context['total']
        context['tax'] = quote.pre_tax_final*TAX_RATE
        context['unit_final'] = quote.pre_tax_final*(1+TAX_RATE)
        context['final'] = context['unit_final']*quote.sample_number
        return context


class QuoteCreateView(LoginRequiredMixin, PermissionRequiredMixin, generic.base.TemplateView):
    permission_required = 'quotes.add_quote'
    raise_exception = True

    template_name = 'quotes/quote_form.html'

    def get(self, request, **kwargs):
        form = QuoteForm()

        return render(request, self.template_name, {'form': form})

    def post(self, request, **kwargs):
        form = QuoteForm(request.POST)

        if form.is_valid():
            new_quote = form.save(commit=False)
            new_quote.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('quotes:detail', kwargs={'pk': new_quote.pk}))

        else:
            # raise ValidationError({'field_name': ["error message",]})
            return HttpResponseRedirect(reverse('quotes:quote-create'))


class QuoteUpdateView(LoginRequiredMixin, PermissionRequiredMixin, generic.base.TemplateView):
    permission_required = 'quotes.change_quote'
    raise_exception = True

    template_name = 'quotes/quote_form.html'

    def get(self, request, **kwargs):
        pk = kwargs['pk']
        quote = get_object_or_404(Quote, pk=pk)
        form = QuoteForm(instance=quote)

        return render(request, self.template_name, {'form': form})

    def post(self, request, **kwargs):
        pk = kwargs['pk']
        quote = get_object_or_404(Quote, pk=pk)
        form = QuoteForm(request.POST, instance=quote)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('quotes:detail', kwargs={'pk': pk}))


class QuoteDeleteView(LoginRequiredMixin, PermissionRequiredMixin, generic.base.TemplateView):
    permission_required = 'quotes.delete_quote'
    raise_exception = True

    template_name = 'jobs/job_confirm_delete.html'
    success_url = 'quotes:index'

    def post(self, request, **kwargs):
        pk = kwargs['pk']
        quote = get_object_or_404(Quote, pk=pk)
        quote.delete()

        return HttpResponseRedirect(reverse(self.success_url))


class ConvertToOrderView(LoginRequiredMixin, PermissionRequiredMixin, generic.base.TemplateView):
    permission_required = ('quotes.view_quote', 'orders.add_order')
    raise_exception = True

    def get(self, request, **kwargs):
        pk = kwargs['pk']
        quote = get_object_or_404(Quote, pk=pk)
        # pdb.set_trace()
        order = Order.objects.create(


            name = quote.name,
            client = quote.client,
            order_date = quote.quote_date,
            payment = quote.payment,
            status = OrderStatus.objects.get(pk = 1),
            service_package = quote.service_package,
            sample_number = quote.sample_number,
            pre_tax_final = quote.pre_tax_final,
            quote = quote,
            # services = quote.services,

        )
        # for service in quote.services
        order.services.add(*quote.services.all())

        return  HttpResponseRedirect(reverse('orders:detail', kwargs={'pk': order.pk}))