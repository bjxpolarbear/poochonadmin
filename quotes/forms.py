from django import forms
import datetime

from .models import Quote
from structure.models import Procedure, Service, ServicePackage
from structure.forms import ProcedureModelMultipleChoiceField

class QuoteForm(forms.ModelForm):
    quote_date = forms.DateField(widget=forms.SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day")
    ), initial=datetime.datetime.now())

    expire_date = forms.DateField(widget=forms.SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day")
    ), initial=(datetime.datetime.now() + datetime.timedelta(30)))

    queryset = ServicePackage.objects.all()
    service_package = forms.ModelChoiceField(queryset=queryset)
    queryset = Service.objects.all()
    services = forms.ModelMultipleChoiceField(queryset=queryset, widget=forms.CheckboxSelectMultiple())

    # queryset = Procedure.get_tree(parent=None)
    # procedures = ProcedureModelMultipleChoiceField(queryset=queryset, widget=forms.CheckboxSelectMultiple())
    #

    class Meta:
        model = Quote
        fields = [
            'name',
            'client',
            'quote_date',
            'expire_date',
            'sample_number',
            'payment',
            'status',
            'service_package',
            'services',
            'pre_tax_final'

        ]

