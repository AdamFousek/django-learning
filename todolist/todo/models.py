from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    parent_category = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE)
    slug = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Todo(models.Model):
    NOT_STARTED = 'not-started'
    IN_PROGRESS = 'in-progress'
    STUCK = 'stuck'
    DONE = 'done'
    STATUS_CHOICES = [
        (NOT_STARTED, 'Not started'),
        (IN_PROGRESS, 'In progress'),
        (STUCK, 'Stuck'),
        (DONE, 'Done'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=12,
        choices=STATUS_CHOICES,
        default=NOT_STARTED,
    )

    def is_overdue_date(self):
        return self.due_date <= timezone.now()

    def __str__(self):
        return "{} - {}".format(self.title, self.get_status_display())
