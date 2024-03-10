from django.db import models

class Payroll(models.Model):
    name = models.CharField(max_length=100)
    rate_of_pay = models.DecimalField(max_digits=6, decimal_places=2)
    hours_worked = models.DecimalField(max_digits=6, decimal_places=2)
