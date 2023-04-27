from django.views import generic

from task_app.models import Task


class TasksListView(generic.ListView):
    model = Task
    template_name = 'task_app/index.html'
    context_object_name = 'task_list'


class TaskDetailView(generic.DetailView):
    model = Task
    template_name = 'task_app/task_detail.html'
    context_object_name = 'task'
