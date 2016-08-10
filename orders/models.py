from django.db import models
from clients.models import Client
from structure.models import PaymentTerm, OrderStatus, ServicePackage, Service
from quotes.models import Quote

class OrderManager(models.Manager):
    def create_book(self, **kwargs):

        order = self.create(
            name=kwargs['name'],
            client=kwargs['client'],
            order_date=kwargs['order_date'],
            payment=kwargs['payment'],
            status=kwargs['status'],
            service_package=kwargs['service_package'],
            services=kwargs['services'],
            sample_number=kwargs['sample_number'],
            pre_tax_final=kwargs['pre_tax_final'],
            quote=kwargs['quote'],

        )
        # do something with the book
        return order


class Order(models.Model):

    name = models.CharField(db_column='Name', max_length=255)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)

    order_date = models.DateField(db_column='Order_Date')

    payment = models.ForeignKey(PaymentTerm, on_delete=models.PROTECT)
    status = models.ForeignKey(OrderStatus, on_delete=models.PROTECT)
    service_package = models.ForeignKey(ServicePackage, blank=True, null=True)
    services = models.ManyToManyField(Service, blank=True)
    sample_number = models.IntegerField(db_column='Sample_Number')

    pre_tax_final = models.FloatField(db_column='Pre_Tax_Final')

    quote = models.ForeignKey(Quote, on_delete=models.PROTECT, null=True)
    objects = OrderManager()

    class Meta:
        permissions = (
            ("view_order", "Can view order"),
        )

    def __str__(self):
        return self.client.__str__() + ': ' + self.name

    def get_services(self):
        services = []
        for service in self.services.all():
            if service not in services:
                services.append(service)
        for service in self.service_package.services.all():
            if service not in services:
                services.append(service)
        return services

    def fill_procedure(self):
        procedures = self.procedures.all()
        added_procedure = []    # Buffer for newly added procedures
        # filling the ancestors
        for procedure in procedures:
            ancestors = procedure.get_ancestors()
            for ancestor in ancestors:
                if ancestor not in procedures or added_procedure:
                    self.procedures.add(ancestor)
                    added_procedure.append(ancestor)