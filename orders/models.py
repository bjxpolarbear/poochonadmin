from django.db import models
from clients.models import Client
from structure.models import PaymentTerm, OrderStatus, ServicePackage, Service


class Order(models.Model):

    name = models.CharField(db_column='Name', max_length=255)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)

    order_date = models.DateField(db_column='Order_Date')

    payment = models.ForeignKey(PaymentTerm, on_delete=models.PROTECT)
    status = models.ForeignKey(OrderStatus, on_delete=models.PROTECT)
    service_package = models.ForeignKey(ServicePackage, blank=True, null=True)
    services = models.ManyToManyField(Service, blank=True)
    sample_number = models.IntegerField(db_column='Sample_Number')


    class Meta:
        permissions = (
            ("view_order", "Can view order"),
        )

    def __str__(self):
        return self.client + ': ' + self.name
