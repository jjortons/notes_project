from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Note


class NoteListView(ListView):
    model = Note
    template_name = 'notes_app/note_list.html'
    context_object_name = 'notes'
    paginate_by = 10


class NoteDetailView(DetailView):
    model = Note
    template_name = 'notes_app/note_detail.html'


class NoteCreateView(CreateView):
    model = Note
    fields = ['title', 'category', 'content', 'date_taken', 'icon']
    template_name = 'notes_app/note_form.html'
    success_url = reverse_lazy('note_list')

    def form_valid(self, form):
        messages.success(self.request, 'Note created successfully!')
        return super().form_valid(form)


class NoteUpdateView(UpdateView):
    model = Note
    fields = ['title', 'category', 'content', 'date_taken', 'icon']
    template_name = 'notes_app/note_form.html'
    success_url = reverse_lazy('note_list')

    def form_valid(self, form):
        messages.success(self.request, 'Note updated successfully!')
        return super().form_valid(form)


class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'notes_app/note_confirm_delete.html'
    success_url = reverse_lazy('note_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Note deleted successfully!')
        return super().delete(request, *args, **kwargs)
