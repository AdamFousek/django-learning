from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import Todo
from django.urls import reverse
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'todo/index.html'
    context_object_name = 'latest_todo_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Todo.objects.exclude(status=Todo.DONE).order_by('-created_at')[:5]


class DetailView(generic.DetailView):
    model = Todo
    template_name = 'todo/detail.html'


def change_status(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    selected_status = request.POST['status']
    todo.status = selected_status
    todo.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('todo:detail', args=(todo.id,)))
