from django.shortcuts import render, redirect

from app15.form import CourseCreate, ModuleCreate, LessonCreate
from app15.models import Course, Module, Lesson


# Create your views here.

def course_list_view(request):
    context = {'course_list':Course.objects.all()}
    return render(request, 'course_list.html', context)
def course_detail(request, pk):
    context = {'course':Course.objects.get(pk=pk), 'module_list':Module.objects.filter(course=Course.objects.get(pk=pk))}
    return render(request, 'course_detail.html', context)
def module_detail(request, pk):
    context = {'module':Module.objects.get(pk=pk), 'lesson_list':Lesson.objects.filter(module=Module.objects.get(pk=pk)),'cb_pk':Module.objects.get(pk=pk).course.pk}
    return render(request,'module_detail.html', context)
def lesson_detail(request, pk):
    context = {'lesson':Lesson.objects.get(pk=pk), 'cb_pk':Lesson.objects.get(pk=pk).module.pk}
    return render(request, 'lesson_detail.html', context)



def create_course(request):
    context = {}
    if request.method == 'POST':
        form = CourseCreate(request.POST)
        if form.is_valid():
            form.save()
        return redirect('course_list')
    form = CourseCreate()
    context['form'] = form
    return render(request, 'create/course.html', context)
def create_module(request, pk):
    context = {}
    if request.method == 'POST':
        form = ModuleCreate(request.POST)
        if form.is_valid():
            form.save()

        return redirect('course_detail', pk=pk)
    form = ModuleCreate()
    context['form'] = form
    return render(request, 'create/module.html', context)
def create_lesson(request, pk):
    context = {}
    if request.method == 'POST':
        form = LessonCreate(request.POST)
        if form.is_valid():
            form.save()

        return redirect('module_detail', pk=pk)
    form = LessonCreate()
    context['form'] = form
    return render(request, 'create/lesson.html', context)



def update_course(request, pk):
    context = {}
    if request.method == 'POST':
        form = CourseCreate(request.POST, instance=Course.objects.get(pk=pk))
        if form.is_valid():
            form.save()

        return redirect('course_list')
    form = CourseCreate(
        initial={'title': Course.objects.get(pk=pk).title,
                 'description': Course.objects.get(pk=pk).description,
                 'avarge_time': Course.objects.get(pk=pk).avarge_time})
    context['form'] = form
    return render(request, 'update/course.html', context)
def update_module(request, pk):
    context = {}
    if request.method == 'POST':
        form = ModuleCreate(request.POST, instance=Module.objects.get(pk=pk))
        if form.is_valid():
            form.save()

        return redirect('course_detail', pk=Module.objects.get(pk=pk).course.pk)
    form = ModuleCreate(
        initial={'course': Module.objects.get(pk=pk).course,
                 'title': Module.objects.get(pk=pk).title,
                 'description': Module.objects.get(pk=pk).description,
                 'avarge_time': Module.objects.get(pk=pk).avarge_time})
    context['form'] = form
    return render(request, 'update/module.html', context)
def update_lesson(request, pk):
    context = {}
    if request.method == 'POST':
        form = LessonCreate(request.POST, instance=Lesson.objects.get(pk=pk))
        if form.is_valid():
            form.save()

        return redirect('module_detail', pk=Lesson.objects.get(pk=pk).module.pk)
    form = LessonCreate(
        initial={'module': Lesson.objects.get(pk=pk).module,
                 'title': Lesson.objects.get(pk=pk).title,
                 'content': Lesson.objects.get(pk=pk).content,
                 'duration_time': Lesson.objects.get(pk=pk).duration_time})
    context['form'] = form
    return render(request, 'update/module.html', context)



def delete_course(request, pk):
    course = Course.objects.get(pk=pk)
    course.delete()
    return redirect('course_list')
def delete_module(request, pk):
    module = Module.objects.get(pk=pk)
    module.delete()
    return redirect('course_detail')
def delete_lesson(request, pk):
    lesson = Lesson.objects.get(pk=pk)
    lesson.delete()
    return redirect('module_detail')
