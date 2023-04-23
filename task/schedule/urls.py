from django.urls import path
from .views import MainView, CourseView, TeacherView, AddCourseView, MySignupView, MyLoginView
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='schedule-main')),
    path('schedule/main/', MainView.as_view(), name="schedule-main"),
    path('schedule/course_details/<int:course_id>', CourseView.as_view()),
    path('schedule/teacher_details/<int:teacher_id>', TeacherView.as_view()),
    path('schedule/add_course/', AddCourseView.as_view()),
    path('signup/', MySignupView.as_view()),
    path('login/', MyLoginView.as_view()),
]