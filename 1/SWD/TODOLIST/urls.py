from django.urls import path
from . import views

urlpatterns = [
    path('',views.todolst, name='todolst'),
    path('delete/<int:todo_id>', views.delete, name='delete'),
    path('status/<int:todo_id>', views.status, name='status')
]