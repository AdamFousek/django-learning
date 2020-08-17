import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Todo, Category


def create_todo_with_date(self, date):
    category = Category(name="School", slug="school")
    todo = Todo(
        title="Test",
        description="Test description",
        due_date=date,
        category=category
    )

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
