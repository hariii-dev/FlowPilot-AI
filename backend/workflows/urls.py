from django.urls import path
from .views import WorkflowListCreateView, WorkflowDetailView

urlpatterns = [
    path('', WorkflowListCreateView.as_view(), name='workflow-list-create'),
    path('<int:pk>/', WorkflowDetailView.as_view(), name='workflow-detail'),
]
