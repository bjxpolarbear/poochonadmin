from django.db import models
from clients.models import Client
from structure.models import Service, ServicePackage, PaymentTerm, QuoteStatus, Procedure


class Quote(models.Model):

    name = models.CharField(db_column='Name', max_length=255)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)

    quote_date = models.DateField(db_column='Quote_Date')
    expire_date = models.DateField(db_column='Expire_Date')
    payment = models.ForeignKey(PaymentTerm, on_delete=models.PROTECT)
    status = models.ForeignKey(QuoteStatus, on_delete=models.PROTECT)
    service_package = models.ForeignKey(ServicePackage, blank=True, null=True)
    services = models.ManyToManyField(Service, blank=True)
    sample_number = models.IntegerField(db_column='Sample_Number')

    pre_tax_final = models.FloatField(db_column='Pre_Tax_Final')


    class Meta:
        permissions = (
            ("view_quote", "Can view quote"),
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


        # procedures = sorted(procedures,key=lambda procedure: procedure.path)
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
