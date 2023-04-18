from django.db import models

# Create your models here.


class Section(models.Model):
    title = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'

    def __str__(self):
        return self.title

class Division(models.Model):
    title = models.CharField(max_length=250)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Division'
        verbose_name_plural = 'Divisions'

    def __str__(self):
        return self.title
