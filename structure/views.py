from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic
from django.core import serializers


from django.utils.functional import Promise
from django.utils.encoding import force_text
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from .models import Service, ServicePackage, Procedure, QuoteStatus, OrderStatus, JobStatus
# Create your views here.


class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Promise):
            return force_text(obj)
        return super(LazyEncoder, self).default(obj)


class StructureIndexView(LoginRequiredMixin, PermissionRequiredMixin, generic.TemplateView):
    permission_required = ('structure.view_service','structure.view_servicepackage')
    template_name = 'structure/index.html'
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super(StructureIndexView, self).get_context_data(**kwargs)

        context['packages'] = ServicePackage.objects.all()
        context['services'] = Service.objects.all()
        context['procedures'] = Procedure.objects.all()
        context['quotestatuses'] = QuoteStatus.objects.all()
        context['orderstatuses'] = OrderStatus.objects.all()
        context['jobstatuses'] = JobStatus.objects.all()

        return context

class ServicePackageJsonView(LoginRequiredMixin, PermissionRequiredMixin, generic.View):
    permission_required = 'structure.view_servicepackage'


    def get(self, request):
        allServicePackages = ServicePackage.objects.all()
        return JsonResponse(serializers.serialize('json', allServicePackages), safe=False)

class ServiceJsonView(LoginRequiredMixin, PermissionRequiredMixin, generic.View):
    permission_required = 'structure.view_service'

    def get(self, request):

        allServices = Service.objects.all()
        return JsonResponse(serializers.serialize('json', allServices), safe=False)