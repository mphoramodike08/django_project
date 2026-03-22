from django import forms

from .models import Note


class NoteForm(forms.ModelForm):
    """Form used to create and update note records."""

    class Meta:
        model = Note
        fields = ["title", "content"]
