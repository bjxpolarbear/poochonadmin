from django import forms
import datetime

from .models import Item


class ItemForm(forms.ModelForm):

    date_received = forms.DateField(widget=forms.SelectDateWidget(),initial=datetime.datetime.now)

    class Meta:
        model = Item
        fields = [
            'name',
            'item_id',
            'category',
            'unit',
            'quantity',
            'unit_price',
            'date_received',
            'location',
            'description',
        ]