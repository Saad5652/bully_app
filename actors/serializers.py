from rest_framework import serializers

from .models import Parent, Teacher, Student
from entities.serializers import DivisionSerializer


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ['id', 'name', 'phone_number',]


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'name', 'image',]


class StudentSerializerFull(serializers.ModelSerializer):
    parent = ParentSerializer()
    division = DivisionSerializer()

    class Meta:
        model = Student
        fields = ['id', 'name', 'parent', 'division', 'image', 'gender', ]


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'parent', 'division', 'image', 'gender', ]

    def to_representation(self, instance):
        if self.context['request'].method == "GET":
            serializer = StudentSerializerFull(instance)
            return serializer.data
        return super().to_representation(instance)
