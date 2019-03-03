from django.shortcuts import render
from .models import Ticket
from .forms import TicketForm
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import permission_required


# Create your views here.
@permission_required('ticket.view_ticket', login_url="/accounts/login")
def show_tickets(request):
    tickets = Ticket.objects.filter(status="Created")
    return render(request, 'core/unresolved.html', {'tickets': tickets})


def show_options(request):
    return render(request, 'core/home.html', {})


@permission_required('ticket.view_ticket', login_url="/accounts/login")
def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    return render(request, 'core/ticket_detail.html', {'ticket': ticket})


@permission_required('ticket.view_ticket', login_url="/accounts/login")
def show_closed_tickets(request):
    tickets = Ticket.objects.filter(status="Closed")
    return render(request, 'core/closed_tickets.html', {'tickets': tickets})


@permission_required('ticket.view_ticket', login_url="/accounts/login")
def close_ticket(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == "POST":
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.resolved_time = timezone.now()
            ticket.status = "Closed"
            ticket.save()
            return redirect('show_closed_tickets')
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'core/close_ticket.html', {'form': form})


