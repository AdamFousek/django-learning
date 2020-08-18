from django.contrib import admin

# Register your models here.
from .models import Todo, Category


class TodoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic Information', {'fields': ['title', 'description']}),
        ('Advance Information', {'fields': ['category', 'due_date']}),
    ]
    list_display = ('title', 'category', 'is_overdue_date', 'due_date')
    list_filter = ['due_date']
    search_fields = ['title', 'description']


admin.site.register(Todo, TodoAdmin)
admin.site.register(Category)
