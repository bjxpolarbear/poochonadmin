from django import forms
import datetime

from .models import Order
from structure.models import Procedure, Service, ServicePackage
from structure.forms import ProcedureModelMultipleChoiceField

class OrderForm(forms.ModelForm):
    order_date = forms.DateField(widget=forms.SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day")
    ), initial=datetime.datetime.now())


    queryset = ServicePackage.objects.all()
    service_package = forms.ModelChoiceField(queryset=queryset)
    queryset = Service.objects.all()
    services = forms.ModelMultipleChoiceField(queryset=queryset, widget=forms.CheckboxSelectMultiple())


    class Meta:
        model = Order
        fields = [
            'name',
            'client',
            'order_date',
            'quote',
            'sample_number',
            'payment',
            'status',
            'service_package',
            'services',
            'pre_tax_final'

        ]

