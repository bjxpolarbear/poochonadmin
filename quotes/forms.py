from django import forms
import datetime

from .models import Quote, Sample
from structure.forms import ProcedureForm as QuoteProcedureForm


class QuoteForm(forms.ModelForm):
    quote_date = forms.DateField(widget=forms.SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day")
    ), initial=datetime.datetime.now())

    expire_date = forms.DateField(widget=forms.SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day")
    ), initial=(datetime.datetime.now() + datetime.timedelta(30)))

    class Meta:
        model = Quote
        fields = [
            'name',
            'client',
            'quote_date',
            'expire_date',
            'payment',
            'status',
            'job_type'
        ]


class SampleForm(forms.ModelForm):
    date_received = forms.DateField(widget=forms.SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day")
    ), initial=datetime.datetime.now)

    class Meta:
        model = Sample
        fields = [
            'name',
            'sample_type',
            'organism',
            'sample_status',
            'date_received',
            'location',
            'storage',
            'client',
            'quote',
            'job',

        ]
