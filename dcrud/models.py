from django.db import models

# Create your models here.
class Record(models.Model):
    create_date = models.DateTimeField(auto_now=True)
    Description=models.CharField(max_length=100)
    Proposal_amount=models.IntegerField()
    Provision_availed=models.IntegerField()
    PartyName=models.CharField(max_length=100)
    # Balance=models.IntegerField()
    def Balance(self):
        return self.Proposal_amount - self.Provision_availed

    def __str__(self):
        return (f"{self.Description} {self.PartyName}")
    




    