from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

# Create your views here.


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    success_message = "%(username)s account created!"


class UserUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'users/profile.html'
    fields = ['email']
    success_url = reverse_lazy('users:profile')
    success_message = "Информация изменена"

    def get_object(self):
        return self.request.user
