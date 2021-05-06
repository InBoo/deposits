from django.forms import ModelForm

from deposits import models


# https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/#creating-forms-from-models
class DepositForm(ModelForm):
    class Meta:
        model = models.Deposit
        fields = ['deposit', 'term', 'rate']
        labels = {
            'deposit': 'Deposit (euro)',
            'term': 'Term (years)',
            'rate': 'Rate (decimal)',
        }

