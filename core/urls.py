from django.urls import path
from . import views

urlpatterns = [
    path('unresolved/', views.show_tickets, name="show_tickets"),
    path('', views.show_options, name="show_options"),
    path('home', views.show_options, name="show_options"),
    path('unresolved/<int:pk>/', views.ticket_detail, name='ticket_detail'),
    path('unresolved/<int:pk>/close/', views.close_ticket, name='close_ticket'),
    path('closed', views.show_closed_tickets, name='show_closed_tickets'),
    path('create/', views.create_ticket, name="create_ticket"),
    path('ajax/validate_student_id/', views.validate_student_id, name="validate_student_id")
]
