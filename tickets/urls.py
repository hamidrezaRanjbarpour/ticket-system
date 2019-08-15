from django.urls import path, include
from . import views

app_name = 'tickets'

urlpatterns = [
    path('', views.ListOfTickets.as_view(), name='list_of_tickets'),
    path('<int:pk>/', views.detail_view, name='detail'),

]