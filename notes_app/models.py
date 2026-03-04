from django.db import models


class Note(models.Model):
    # User-inputted fields
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    date_taken = models.DateField()

    # Optional icon image for this note
    icon = models.ImageField(upload_to='note_icons/', blank=True, null=True)

    # Automatically handled fields
    date_added = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title
