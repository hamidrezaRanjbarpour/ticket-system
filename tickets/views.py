from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, reverse
from .forms import TicketForm
from django.views import generic
from .models import Ticket
# Create your views here.


class ListOfTickets(generic.ListView):
    context_object_name = 'tickets'
    template_name = 'tickets/ticket_list.html'

    def get_queryset(self):
        return Ticket.objects.filter(owner=self.request.user)


class DetailsView(generic.DetailView):
    model = Ticket
    template_name = 'tickets/ticket_details.html'

    def get_queryset(self):
        return Ticket.objects.filter(owner=self.request.user)


def detail_view(request, pk):
    ticket = get_object_or_404(Ticket, id=pk)
    if request.method == 'POST':
        comment = request.POST.get('comment')
        ticket.comment_set.create(owner=ticket.owner, content=comment)
        return HttpResponseRedirect(reverse('tickets:detail', args=(pk,)))

    return render(request, 'tickets/ticket_details.html', {'ticket': ticket})
