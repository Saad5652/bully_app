from rest_framework import serializers

from .models import Report


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('id', 'culprit_type', 'description', 'content_type', 'object_id', 'content_object', 'victim', 'date_created', )


