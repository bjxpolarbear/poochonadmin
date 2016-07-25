from django import forms
from .models import Job, Procedure
import datetime

import pdb

#  customize the display of job form
class ProcedureModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.indented_name()


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

class JobProcedureForm(forms.Form):
    queryset = Procedure.get_tree(parent=None)
    procedure = ProcedureModelMultipleChoiceField(queryset=queryset,widget=forms.CheckboxSelectMultiple())