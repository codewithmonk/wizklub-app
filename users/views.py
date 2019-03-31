from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import permission_required
from django.contrib import messages


@permission_required('user.add_user', login_url="/user_not_permitted/")
def create_user(request):
    if request.method == 'POST':
        custom_form = CustomUserCreationForm(request.POST)
        if custom_form.is_valid():
            custom_form.save()
            messages.success(request, 'Account created successfully')
            return redirect('show_options')

    else:
        custom_form = CustomUserCreationForm()

    return render(request, 'users/create_user.html', {'form': custom_form})


def show_invalid_permission(request):
    return render(request, 'users/user_not_permitted.html', {})

