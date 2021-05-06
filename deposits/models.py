from django.db import models

class Deposit(models.Model):
    deposit = models.FloatField()
    term = models.IntegerField()
    rate = models.FloatField()
    interest = models.FloatField()

    def __str__(self):
        return 'Deposit: {deposit}, Term: {term}, Rate: {rate}, Interest: {interest}'.format(deposit=self.deposit, term=self.term, rate=self.rate, interest=self.interest)


