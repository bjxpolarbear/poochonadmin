from django import forms

from .models import Procedure

#  customize the display of job form
class ProcedureModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.indented_name()


class ProcedureForm(forms.Form):
    queryset = Procedure.get_tree(parent=None)
    procedure = ProcedureModelMultipleChoiceField(queryset=queryset, widget=forms.CheckboxSelectMultiple())