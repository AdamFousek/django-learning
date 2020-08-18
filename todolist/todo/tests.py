import datetime

from django.utils.crypto import get_random_string
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from todo.models import Todo, Category


def create_todo_with_date(date):
    category, created = Category.objects.get_or_create(
        name="School", slug="school")
    todo = Todo(
        title=get_random_string(10),
        description=get_random_string(100),
        due_date=date,
        category=category,
    )
    todo.save()

    return todo


class TodoModelTests(TestCase):

    def test_is_overdue_date_future_date(self):
        """
        is_overdue_date() returns false if due_date is in future otherwise return true
        """
        future_time = timezone.now() + datetime.timedelta(days=10)
        todo = create_todo_with_date(future_time)
        self.assertIs(todo.is_overdue_date(), False)

    def test_is_overdue_date_past_date(self):
        past_time = timezone.now() - datetime.timedelta(days=10)
        todo = create_todo_with_date(past_time)
        self.assertIs(todo.is_overdue_date(), True)


class TodoIndexViewTests(TestCase):

    def test_no_todo(self):
        response = self.client.get(reverse('todo:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_todo_list'], [])

    def test_one_todo(self):
        future_time = timezone.now() + datetime.timedelta(days=10)
        todo = create_todo_with_date(future_time)
        response = self.client.get(reverse('todo:index'))
        self.assertEqual(len(response.context['latest_todo_list']), 1)
        todo.delete()

    def test_one_done_one_not_done(self):
        future_time = timezone.now() + datetime.timedelta(days=10)
        todo_not_done = create_todo_with_date(future_time)
        todo_done = create_todo_with_date(future_time)
        todo_done.status = Todo.DONE
        todo_done.save()
        response = self.client.get(reverse('todo:index'))
        self.assertEqual(len(response.context['latest_todo_list']), 1)
        todo_not_done.delete()
        todo_done.delete()
