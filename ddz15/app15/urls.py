from django.urls import path

from app15.views import create_course, create_module, create_lesson, update_course, update_module, update_lesson, \
    course_list_view, course_detail, module_detail, lesson_detail, delete_course, delete_module, delete_lesson

urlpatterns = [
    path('', course_list_view, name='course_list'),
    path('course-detail/<int:pk>', course_detail, name='course_detail'),
    path('module-detail/<int:pk>', module_detail, name='module_detail'),
    path('lesson-detail/<int:pk>', lesson_detail, name='lesson_detail'),

    path('create-course/', create_course, name='create_course'),
    path('create-module/<int:pk>', create_module, name='create_module'),
    path('create-lesson/<int:pk>', create_lesson, name='create_lesson'),

    path('update-course/<int:pk>', update_course, name='update_course'),
    path('update-module/<int:pk>', update_module, name='update_module'),
    path('update-lesson/<int:pk>', update_lesson, name='update_lesson'),

    path('delete-course/<int:pk>', delete_course, name='delete_course'),
    path('delete-module/<int:pk>', delete_module, name='delete_module'),
    path('delete-lesson/<int:pk>', delete_lesson, name='delete_lesson'),

]