from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import Todo
from django.urls import reverse, reverse_lazy


class IndexView(generic.ListView):
    template_name = 'todo/index.html'
    context_object_name = 'todos'
    model = Todo

    def get_queryset(self):
        """
        Returns all todos split into dict by status
        """
        todo = {
            Todo.NOT_STARTED: Todo.objects.filter(status=Todo.NOT_STARTED),
            Todo.IN_PROGRESS: Todo.objects.filter(status=Todo.IN_PROGRESS),
            Todo.DONE: Todo.objects.filter(status=Todo.DONE),
            Todo.STUCK: Todo.objects.filter(status=Todo.STUCK),
        }

        return todo

    def get_context_data(self):
        '''
        Adds the model to the context data.
        '''
        context = super(generic.ListView, self).get_context_data()
        context['todoModel'] = self.model
        return context


class DetailView(generic.DetailView):
    model = Todo
    template_name = 'todo/detail.html'

    def get_context_data(self, **kwargs):
        '''
        Adds the model to the context data.
        '''
        context = super(generic.DetailView, self).get_context_data(**kwargs)
        context['todoModel'] = self.model
        return context


class RemoveView(generic.edit.DeleteView):
    model = Todo
    success_url = reverse_lazy('index')


def change_status(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    selected_status = request.POST['status']
    todo.status = selected_status
    todo.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('todo:detail', args=(todo.id,)))
