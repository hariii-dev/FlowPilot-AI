from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Workflow
from .serializers import WorkflowSerializer
from organizations.models import Organization


class WorkflowListCreateView(generics.ListCreateAPIView):
    serializer_class = WorkflowSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Workflow.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        organization_id = self.request.data.get('organization')

        organization = Organization.objects.get(
            id=organization_id,
            owner=self.request.user
        )

        serializer.save(
            owner=self.request.user,
            organization=organization
        )


class WorkflowDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkflowSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Workflow.objects.filter(owner=self.request.user)

