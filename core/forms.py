from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        model.resolution.editable = True
        fields = ('resolution', )


class NewTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('concerned_department', 'issue_type', 'student_name', 'current_skill', 'comment')




