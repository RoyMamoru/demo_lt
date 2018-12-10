from django.db import models
from datetime import date


class Customers(models.Model):
    # 選択式のものをここで定義（左：実際にDBに格納される値、右：UIに表示される値）
    education_options = (
    (1, 'graduate_school'),
    (2, 'university'),
    (3, 'high school'),
    (4, 'other'),
    )

    marital_options = (
    (1, 'married'),
    (2, 'single'),
    (3, 'others')
    )

    gender_options = (
    (1,'male'),
    (2,'female'),
    )

    payment_history = (
    (-1, 'pay early'),
    (0, 'pay dully'),
    (1, '1month_dalay'),
    (2, '2months_dlay')
    )

    # DBのカラムに相当する部分の定義
    id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    limit_balance = models.IntegerField()
    sex = models.IntegerField(choices=gender_options)
    education = models.IntegerField(choices=education_options)
    marriage = models.IntegerField(choices=marital_options)
    age = models.IntegerField()
    pay_0 = models.IntegerField(choices=payment_history)
    pay_2 = models.IntegerField(choices=payment_history)
    pay_3 = models.IntegerField(choices=payment_history)
    pay_4 = models.IntegerField(choices=payment_history)
    pay_5 = models.IntegerField(choices=payment_history)
    pay_6 = models.IntegerField(choices=payment_history)
    bill_amt_1 = models.IntegerField()
    pay_amt_1 = models.IntegerField()
    pay_amt_2 = models.IntegerField()
    pay_amt_3 = models.IntegerField()
    pay_amt_4 = models.IntegerField()
    pay_amt_5 = models.IntegerField()
    pay_amt_6 = models.IntegerField()
    result = models.IntegerField(blank=True, null=True)
    proba = models.FloatField(default=0.0)
    comment = models.CharField(max_length=200, blank=True, null=True)
    registered_date = models.DateField(
            default=date.today())

    def register(self):
        self.registered_date = date.today()
        self.save()

    def __str__(self):
        if self.proba == 0.0:
            return '%s, %d, %s' % (self.registered_date.strftime('%Y-%m-%d'), self.id, self.last_name+self.first_name)
        else:
            return '%s, %d, %s, %d, %s, %s' % (self.registered_date.strftime('%Y-%m-%d'), self.id, self.last_name+self.first_name, self.result, '{}%'.format(round(self.proba*100, 2)), self.comment)
