from django.db import models
from actors.models import Student, Teacher


class Report(models.Model):
    TEACHER = 'teacher'
    STUDENT = 'student'
    CULPRIT_TYPES = (
        (TEACHER, 'Teacher'),
        (STUDENT, 'Student'),
    )

    culprit_type = models.CharField(max_length=15, choices=CULPRIT_TYPES)

    description = models.TextField()

    culprit_teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, blank=True, null=True, related_name="crimes")
    culprit_student = models.ForeignKey(
        Student, on_delete=models.CASCADE, blank=True, null=True, related_name="crimes")

    victim = models.ForeignKey(Student, on_delete=models.CASCADE)

    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Report."""

        verbose_name = 'Report'
        verbose_name_plural = 'Reports'
