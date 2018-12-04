from django.db import models
from django.utils import timezone


class Customers(models.Model):
    id = models.AutoField(primary_key=True)
    limit_balance = models.BigIntegerField()
    sex = models.BigIntegerField()
    education = models.BigIntegerField()
    marriage = models.BigIntegerField()
    age = models.BigIntegerField()
    pay_0 = models.BigIntegerField()
    pay_1 = models.BigIntegerField()
    pay_2 = models.BigIntegerField()
    pay_3 = models.BigIntegerField()
    pay_4 = models.BigIntegerField()
    pay_5 = models.BigIntegerField()
    pay_6 = models.BigIntegerField()
    bill_amt_0 = models.BigIntegerField()
    bill_amt_1 = models.BigIntegerField()
    bill_amt_2 = models.BigIntegerField()
    bill_amt_3 = models.BigIntegerField()
    bill_amt_4 = models.BigIntegerField()
    bill_amt_5 = models.BigIntegerField()
    bill_amt_6 = models.BigIntegerField()
    pay_amt_0 = models.BigIntegerField()
    pay_amt_1 = models.BigIntegerField()
    pay_amt_2 = models.BigIntegerField()
    pay_amt_3 = models.BigIntegerField()
    pay_amt_4 = models.BigIntegerField()
    pay_amt_5 = models.BigIntegerField()
    pay_amt_6 = models.BigIntegerField()
    result = models.BigIntegerField()
    proba = models.FloatField()
    comment = models.CharField(max_length=200)
    registered_date = models.DateTimeField(
            default=timezone.now)

    def register(self):
        self.registered_date = timezone.now()
        self.save()

    def __int__(self):
        return self.result
