from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from actors.models import Student



class Report(models.Model):
    TEACHER = 'T'
    STUDENT = 'S'
    CULPRIT_TYPES = (
        (TEACHER, 'Teacher'),
        (STUDENT, 'Student'),
    )

    culprit_type = models.CharField(max_length=1, choices=CULPRIT_TYPES)

    description = models.TextField()

    # Below the mandatory fields for generic relation
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    victim = models.ForeignKey(Student, on_delete=models.CASCADE)

    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Report."""

        verbose_name = 'Report'
        verbose_name_plural = 'Reports'
