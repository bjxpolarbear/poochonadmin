from django.db import models
from django.core.urlresolvers import reverse

from structure.models import ItemCategory


class Item(models.Model):
    name = models.CharField(db_column='Name', max_length=1023)
    item_id = models.CharField(db_column='Item_ID', max_length=127, unique=True, blank=True, null=True)
    category = models.ForeignKey(ItemCategory, on_delete=models.PROTECT)
    unit = models.CharField(db_column='Unit', max_length=63)
    quantity = models.IntegerField(db_column='Quantity')
    unit_price = models.FloatField(db_column='Unit_Price', blank=True, null=True)
    date_received = models.DateField(db_column='Date_Received', blank=True, null=True)

    # ideally location should be another tree stuct and sub_loc is not necessary
    location = models.CharField(db_column='Location', max_length=255)
    description = models.TextField(db_column='Description', blank=True, null=True)

    # I don't feel the payment field is necessay
    # payment = models.CharField(db_column='Location', max_length=255, blank=True, null=True)

    class Meta:
        permissions = (
            ("view_item", "Can view item"),
        )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('inventory:detail', kwargs={'pk': self.id})

