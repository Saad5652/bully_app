from rest_framework import serializers

from .models import Report


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('id', 'culprit_type', 'description', 'culprit_teacher',
                  'culprit_student', 'victim', 'date_created', )
