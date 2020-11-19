from django.shortcuts import render
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            form = user_form.save(commit=False)
            # Set the chosen password
            form.set_password(user_form.cleaned_data['password'])
            # Save the User object
            form.save()
            return render(request, 'registration/register_done.html', {'form': form})
    else:
        form = UserRegistrationForm()
        print('``````````````````````')
    return render(request, 'registration/register.html', {'form': form})