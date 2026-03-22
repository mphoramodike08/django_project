from django.db import models


class Note(models.Model):
    """A single sticky note with a title, content, and creation timestamp."""

    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the note title for admin and shell displays."""
        return self.title
