from django.contrib import admin

from app15.models import Course, Module, Lesson

# Register your models here.

admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Lesson)
