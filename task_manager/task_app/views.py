from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from .models import Task
from django.shortcuts import render


def home_page(request):
    return render(request, "task_app/index.html")


class TasksListView(generic.ListView):
    model = Task
    template_name = 'task_app/task_list.html'
    context_object_name = 'task_list'


class TaskDetailView(generic.DetailView):
    model = Task
    template_name = 'task_app/task_detail.html'
    context_object_name = 'task'


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
