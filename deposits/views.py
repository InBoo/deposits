
from django.views.generic import FormView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from deposits.models import Deposit as DepositDB
from deposits.forms import DepositForm









class Deposit():
    def __init__(self, deposit, term, rate):

        # Sākotnējā noguldīguma summa
        self.deposit = deposit

        # Noguldījuma termiņš gados
        self.term = term

        # Gada procentu likme, decimālskaitlis, 5%=0.05
        self.rate = rate


    # Aprēķina peļņu noguldījuma termiņa beigās
    def interest(self):

        total_interest = 0.0
        year = 0
        while year < self.term:
            interest = self.deposit * self.rate
            total_interest += interest
            self.deposit += interest
            year += 1

        return total_interest
            
            

















# https://docs.djangoproject.com/en/3.2/ref/class-based-views/generic-display/#listview
class DepositListView(ListView):
    model = DepositDB






class DepositDetailView(DetailView):
    model = DepositDB






# https://docs.djangoproject.com/en/3.2/ref/class-based-views/generic-editing/#formview
class AddDepositView(FormView):

    form_class = DepositForm
    template_name = 'deposits/form.html'
    success_url = reverse_lazy('deposits:index')

    def form_valid(self, form):
        deposit_db = form.save(commit=False)
        deposit = Deposit(
            deposit=deposit_db.deposit,
            term=deposit_db.term,
            rate=deposit_db.rate,
        )

        deposit_db.interest = deposit.interest()

        deposit_db.save()


        return super().form_valid(form)
 












