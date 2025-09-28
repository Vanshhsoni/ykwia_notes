# api/views.py
from rest_framework import viewsets, permissions
from paper.models import Note
from .serializers import NoteSerializer

class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]  # only logged-in users can access

    def get_queryset(self):
        # return notes only for the logged-in user
        return Note.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # automatically set the logged-in user as the owner of the note
        serializer.save(user=self.request.user)
