from django.contrib import admin

from .models import Student, Parent, Teacher

admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Teacher)