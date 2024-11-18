from django.urls import path
from .views import TasksView, SingleTaskView

urlpatterns = [
    path('tasks/', TasksView.as_view()),
    path('tasks/<id>/', SingleTaskView.as_view())
]
