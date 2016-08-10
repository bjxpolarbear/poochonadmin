import django_tables2 as tables
from .models import Client


class ClientTable(tables.Table):
    class Meta:
        model = Client
        attrs = {'class': 'paleblue'}
        fields = [
            'customer_id',
            'first_name',
            'last_name',
            'company',

        ]