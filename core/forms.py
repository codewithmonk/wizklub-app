from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        model.resolution.editable = True
        fields = ('resolution', )
