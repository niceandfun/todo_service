from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path('task_list/', views.TasksListView.as_view(), name='task_list'),
    path('task_list/<int:pk>', views.TaskDetailView.as_view(), name='task_detail'),
    path("signup/", views.SignUp.as_view(), name="signup"),
]
