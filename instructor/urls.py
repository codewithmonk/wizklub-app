from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_instructor_list, name='post_instructor_list')
]