from django import forms
from .models import Ticket
from .choices import *

# class TicketForm(forms.Form):
#         pass
#
#
# class TicketModelForm(forms.ModelForm):
#     class Meta:
#         model = Ticket
#         fields = ['title', 'content']


class TicketForm(forms.Form):
    title   = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    priority = forms.ChoiceField(choices=PRIORITY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    attachment = forms.FileField(required=False, widget=forms.FileInput())

    def clean_title(self):
        title = self.cleaned_data['title']
        ticket = Ticket.objects.filter(title__iexact=title)
        if ticket.exists():
            raise forms.ValidationError("A Ticket with this title already exists. Choose different title.")

        return title
