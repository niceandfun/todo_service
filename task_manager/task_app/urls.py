from django.urls import path
from . import views

urlpatterns = [
    path('', views.TasksListView.as_view(), name='task_list'),
    path('tasks/<int:pk>', views.TaskDetailView.as_view(), name='task_detail')
]
