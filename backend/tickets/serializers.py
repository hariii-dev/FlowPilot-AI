from rest_framework import serializers
from .models import Ticket


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = [
            'id',
            'title',
            'description',
            'organization',
            'workflow',
            'created_by',
            'priority',
            'status',
            'created_at',
            'updated_at'
        ]

        read_only_fields = [
            'id',
            'created_by',
            'created_at',
            'updated_at'
        ]

    def validate_organization(self, value):
        if value.owner != self.context['request'].user:
            raise serializers.ValidationError(
                "You cannot use another user's organization."
            )
        return value

    def validate(self, attrs):
        workflow = attrs.get(
            'workflow',
            self.instance.workflow if self.instance else None
        )

        organization = attrs.get(
            'organization',
            self.instance.organization if self.instance else None
        )

        if workflow:
            if workflow.owner_id != self.context['request'].user.id:
                raise serializers.ValidationError({
                    'workflow': "You cannot use another user's workflow."
                })

            if workflow.organization_id != organization.id:
                raise serializers.ValidationError({
                    'workflow': "Workflow must belong to the selected organization."
                })

        return attrs
