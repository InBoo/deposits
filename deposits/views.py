
from django.views.generic import FormView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from deposits.models import Deposit
from deposits.forms import DepositForm

class Deposit():
    def __init__(self, deposit, term, rate):
        self.deposit = deposit
        self.term = term
        self.rate = rate
        self.interest = 0.0

    def interest(self):
        year = 0
        while year < self.term:
            interest = self.deposit * self.rate
            self.interest += interest
            self.deposit += interest
            year += 1

            
            

# https://docs.djangoproject.com/en/3.2/ref/class-based-views/generic-display/#listview
class DepositListView(ListView):
    model = Deposit






# https://docs.djangoproject.com/en/3.2/ref/class-based-views/generic-editing/#formview
class AddDepositView(FormView):

    form_class = DepositForm
    template_name = 'deposit/form.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()

        response = super().form_valid(form)
        return response



