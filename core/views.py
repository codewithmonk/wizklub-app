from .models import Ticket
from .forms import TicketForm, NewTicketForm
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from students.models import Students
from django.http import JsonResponse
import sys
from django.utils import timezone
sys.path.append('../students')
sys.path.append('../users')
from collections import namedtuple


team_deadlines = {
    'Technical Team': 2,
    'Parent Engagement Team': 3,
    'Operation Team': 5,
    'Sales Team': 2,
    'Business Development Team': 1,
    'Content Team': 1
}


def get_ticket_info(request):
    ticket = namedtuple("ticket", "tickets tickets_count")
    tickets = Ticket.objects.filter(status="Created", concerned_department=request.user.get_role_display())
    count = len(tickets)
    return ticket(tickets=tickets, tickets_count=count)


# @permission_required('ticket.view_ticket', login_url="/accounts/login")
@login_required
def show_tickets(request):
    if request.user.username == "wizklub_admin":
        tickets = Ticket.objects.filter(status="Created")
        return render(request, 'core/unresolved.html', {'tickets': tickets})
    tickets = get_ticket_info(request).tickets
    tickets_count = len(tickets)
    return render(request, 'core/unresolved.html', {'tickets': tickets, 'ticket_count': tickets_count})


@login_required
def show_options(request):
    tickets_count = get_ticket_info(request).tickets_count
    print(tickets_count)
    return render(request, 'core/home.html', {"ticket_count": tickets_count})


# @permission_required('ticket.view_ticket', login_url="/accounts/login")
@login_required
def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk,)
    return render(request, 'core/ticket_detail.html', {'ticket': ticket, "ticket_count": get_ticket_info(
        request).tickets_count})


# @permission_required('ticket.view_ticket', login_url="/accounts/login")
@login_required
def show_closed_tickets(request):
    tickets = Ticket.objects.filter(status="Closed")
    return render(request, 'core/closed_tickets.html', {'tickets': tickets, "ticket_count": get_ticket_info(
        request).tickets_count})


# @permission_required('ticket.change_ticket', login_url="/accounts/login")
@login_required
def close_ticket(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == "POST":
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.resolved_time = timezone.now()
            ticket.status = "Closed"
            ticket.closed_by = request.user.username
            ticket.save()
            return redirect('show_closed_tickets')
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'core/close_ticket.html', {'form': form, 'ticket': ticket, "ticket_count": get_ticket_info(
        request).tickets_count})


# @permission_required('ticket.add_ticket', login_url="/accounts/login")
@login_required
def get_student_name(request):
    student = None
    try:
        student = Students.objects.get(id__exact=request.Get.get("id"))
    except Exception as e:
        pass
    if student == None:
        return JsonResponse({"name": ''})
    else:
        return JsonResponse({"name": student.student_name})


@permission_required('ticket.add_ticket', login_url="/user_not_permitted/")
def create_ticket(request):
    if request.method == "POST":
        form = NewTicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.issued_time = timezone.now()
            ticket.opened_by = request.user
            ticket.resolve_by = timezone.now() + timezone.timedelta(days=team_deadlines[ticket.concerned_department])
            ticket.save()
            return redirect('/unresolved/')
        else:
            print("Not Valid!")
    else:
        form = NewTicketForm()
    return render(request, "core/create_ticket.html", {'form': form})


