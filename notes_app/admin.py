from django.contrib import admin
from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'date_taken', 'date_added', 'icon']
    list_filter = ['category', 'date_taken']
    search_fields = ['title', 'content']
