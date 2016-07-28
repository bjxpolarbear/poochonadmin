from django import forms
from .models import Job
from structure.forms import ProcedureForm as JobProcedureForm
import datetime




class JobCreateForm(forms.ModelForm):
    date_submitted = forms.DateField(widget=forms.SelectDateWidget(),initial=datetime.datetime.now)
    date_completed = forms.DateField(widget=forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")),required=False)

    class Meta:
        model = Job
        fields = [
            'job_name',
            'job_type',
            'client',
            'date_submitted',
            'date_completed',
            'job_status'
        ]
