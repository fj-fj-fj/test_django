from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from accounts.models import CustomUser
from accounts.forms import UCreateForm, UChangeForm


class SignUpView(CreateView):
    form_class = UCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


# class PersonUpdateView(UpdateView):
#     model = CustomUser
#     form_class = UChangeForm
#     template_name = 'accounts/person_update_form.html'
# XXX не пашет падла


def profile_view(request):
    return render(request, 'accounts/profile.html')
