from .models import Final_Year_Projects
from rest_framework import viewsets, permissions, generics
from .serializers import FYPSerializer
from django.db.models.functions import Concat
from django.db.models import Value


# CognitiveViewSet
class FYPViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = FYPSerializer

    def get_queryset(self):
        return self.request.user.records.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class StudentViewSet(viewsets.ModelViewSet):

    queryset = Final_Year_Projects.objects.all()
    serializer_class = FYPSerializer
