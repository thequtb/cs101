"""
Sample model for novice: one table, a few fields.
After editing run: python manage.py makemigrations sample && python manage.py migrate
"""
from django.db import models


class Note(models.Model):
    """Simple note: title and body. created_at is set automatically."""
    title = models.CharField(max_length=15)
    body = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
