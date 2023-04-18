from django.shortcuts import render
from rest_framework import viewsets

from .serializers import ReportSerializer
from .models import Report

class ReportViewset(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer