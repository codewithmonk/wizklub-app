from django.urls import path
from . import views

urlpatterns = [
    path('unresolved/', views.show_tickets, name="show_tickets"),
    path('', views.show_options, name="show_options")
]
