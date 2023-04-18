from rest_framework import serializers

from .models import Section, Division


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['title',]

class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = ['title', 'section',]


