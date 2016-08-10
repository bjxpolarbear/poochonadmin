from django import forms

from .models import Job, Sample
from structure.models import Procedure
from structure.forms import ProcedureModelMultipleChoiceField


import datetime


class JobForm(forms.ModelForm):

    queryset = Procedure.get_tree(parent=None)

    date_submitted = forms.DateField(widget=forms.SelectDateWidget(),initial=datetime.datetime.now)
    date_completed = forms.DateField(widget=forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")),required=False)
    procedures = ProcedureModelMultipleChoiceField(queryset=queryset, widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Job
        fields = [
            'job_name',
            'order',
            'client',
            'date_submitted',
            'date_completed',
            'job_status',
            'procedures'
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
            'order',
            'job',
        ]
