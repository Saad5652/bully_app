from django.db import models

from entities.models import Division


class Parent(models.Model):
    name = models.CharField(max_length=255)
    phone = models.PhoneNumberField()
    

    class Meta:
        verbose_name = 'Parent'
        verbose_name_plural = 'Parents'

    def __str__(self):
        return self.name


def user_directory_path(instance, filename):
    return f'images/user_{instance.user.id}/{filename}'

class Student(models.Model):
    class GENDER_CHOICES(models.Choices):
        male =       ('m', 'male')
        female =    ('f', 'female')
        
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_directory_path, max_length=None, blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES ,max_length=25)


    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.name


class Teacher(models.Model):
    class GENDER_CHOICES(models.Choices):
        male =       ('m', 'male')
        female =    ('f', 'female')

    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=user_directory_path, max_length=None, blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES.choices ,max_length=25)

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    def __str__(self):
        return self.name
