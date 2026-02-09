"""
Sample view: list all Note objects and pass them to the template.
"""
from django.shortcuts import render
from .models import Note


def note_list(request):
    """Show all notes. Template gets variable 'notes'."""
    notes = Note.objects.all()
    return render(request, 'sample/note_list.html', {'notes': notes})
