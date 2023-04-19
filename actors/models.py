from django.db import models

from entities.models import Division


class Parent(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Parent'
        verbose_name_plural = 'Parents'

    def __str__(self):
        return self.name


def user_directory_path(instance, filename):
    return f'images/actors/{filename}'


class Student(models.Model):
    Male = 'M'
    Female = 'F'
    GENDER_CHOICES = (
        (Male, 'Male'),
        (Female, 'Female'),
    )

    name = models.CharField(max_length=255)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to=user_directory_path, max_length=None, blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=25)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.name


class Teacher(models.Model):
    Male = 'M'
    Female = 'F'
    GENDER_CHOICES = (
        (Male, 'Male'),
        (Female, 'Female'),
    )

    name = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to=user_directory_path, max_length=None, blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=25)

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    def __str__(self):
        return self.name
