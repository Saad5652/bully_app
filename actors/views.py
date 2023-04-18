from rest_framework import viewsets

from .models import Parent, Teacher, Student
from .serializers import ParentSerializer, TeacherSerializer, StudentSerializer


class ParentViewset(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

class TeacherViewset(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
