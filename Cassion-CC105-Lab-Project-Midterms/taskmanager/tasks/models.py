from django.db import models
from datetime import date

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)  # Make description optional
    due_date = models.DateField()
    status = models.CharField(max_length=10, default='pending')  # Default to pending

    def is_overdue(self):
        return date.today() > self.due_date

    def display_status(self):
        if self.is_overdue() and self.status != 'complete':
            return 'Overdue'
        return 'Complete' if self.status == 'complete' else 'Pending'

    def __str__(self):
        return self.title
