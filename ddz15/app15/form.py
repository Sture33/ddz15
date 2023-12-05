from django import forms

from app15.models import Course, Module, Lesson


class CourseCreate(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'avarge_time']
        widget = {
            'description': forms.Textarea()
        }
class ModuleCreate(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['course', 'title', 'description', 'avarge_time']
        widget = {
            'course': forms.RadioSelect(),
            'description': forms.Textarea()
        }
class LessonCreate(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['module','title', 'content', 'duration_time']
        widget = {
            'module': forms.RadioSelect(),
            'description': forms.Textarea()
        }
