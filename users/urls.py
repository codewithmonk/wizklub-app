from django.urls import path
from . import views

urlpatterns = [
    # path('create_user/', views.CreateUser.as_view(), name='create_user')
    path('create_user/', views.create_user, name='register'),
    path('user_not_permitted/', views.show_invalid_permission, name='show_invalid_permission')
]
