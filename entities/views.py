from rest_framework import viewsets

from .models import Section, Division
from .serializers import SectionSerializer, DivisionSerializer


class SectionViewset(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class DivisionViewset(viewsets.ModelViewSet):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer



