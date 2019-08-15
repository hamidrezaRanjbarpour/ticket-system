from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from .forms import UserRegisterForm
from tickets.models import Ticket
from tickets.forms import TicketForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def register_view(request):
    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST or None)
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password = register_form.cleaned_data['password']
            email    = register_form.cleaned_data['email']
            first_name = register_form.cleaned_data['first_name']
            last_name = register_form.cleaned_data['last_name']
            new_user = User.objects.create_user(username=username, password=password, email=email)
            new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        register_form = UserRegisterForm()

    return render(request, 'register.html', {'form': register_form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            print(request.user.is_authenticated)
            return HttpResponseRedirect(reverse('index'))
        else:
            if User.objects.filter(username=username).count() > 0:
                return render(request, 'login.html', {'error_message': 'Wrong password for this username!'})
            else:
                return render(request, 'login.html', {'error_message': 'This user has not registered yet!'})
    elif request.method == 'GET':
        return render(request, 'login.html', {})


def logout_view(request):
    username = request.user.username
    logout(request)
    return render(request, 'logout.html', {'username': username})


def create_ticket(request):
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES or None)

        if ticket_form.is_valid():
           title = ticket_form.cleaned_data['title']
           owner = request.user
           content = ticket_form.cleaned_data['content']
           priority = ticket_form.cleaned_data['priority']

           Ticket.objects.create(title=title, owner=owner, content=content, priority=priority)
           return HttpResponseRedirect(reverse('tickets:list_of_tickets'))

    else:
        ticket_form = TicketForm()

    return render(request, 'create_ticket.html', {'form': ticket_form})




