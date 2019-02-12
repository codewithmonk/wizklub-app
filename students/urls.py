from django.urls import path
from . import views

urlpatterns = [
    path('student/search/<int:id>/', views.search_student, name="search_student"),
    path('', views.show_options, name="show_options")
]
