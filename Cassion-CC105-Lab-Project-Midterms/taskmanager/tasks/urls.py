from django.urls import path
from .views import task_list, task_create, task_update, task_delete, task_complete

urlpatterns = [
    path('', task_list, name='task_list'),
    path('create/', task_create, name='task_create'),
    path('update/<int:task_id>/', task_update, name='task_update'),
    path('delete/<int:task_id>/', task_delete, name='task_delete'),
    path('complete/<int:task_id>/', task_complete, name='task_complete'),  # Complete task route
]
