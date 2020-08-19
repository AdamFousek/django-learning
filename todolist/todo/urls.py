from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:todo_id>/change-status/',
         views.change_status, name='change_status'),
    path('<int:pk>', views.RemoveView.as_view(), name='remove')
]
