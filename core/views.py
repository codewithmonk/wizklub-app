from django.shortcuts import render
from .models import Ticket


# Create your views here.
def show_tickets(request):
    tickets = Ticket.objects.filter(status="Created")
    return render(request, 'core/unresolved.html', {'tickets': tickets})


def show_options(request):
    return render(request, 'core/home.html', {})
