from rest_framework import serializers
from .models import Workflow
from organizations.models import Organization


class WorkflowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Workflow
        fields = [
            'id',
            'name',
            'description',
            'organization',
            'owner',
            'status',
            'created_at',
            'updated_at'
        ]

        read_only_fields = [
            'id',
            'owner',
            'created_at',
            'updated_at'
        ]

    def validate_organization(self, value):
        user = self.context['request'].user

        if value.owner != user:
            raise serializers.ValidationError(
                "You cannot use another user's organization."
            )

        return value
