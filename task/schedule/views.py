from django.shortcuts import render, redirect
from django.views import View
from .models import Course, Teacher, Student
from django.http import Http404
from django.forms import ModelForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'surname', 'age', 'course')


class MainView(View):
    def get(self, request):
        q = request.GET.get('q')

        if q is None:
            courses = Course.objects.all()
        else:
            courses = Course.objects.filter(title__contains=q)

        return render(request, 'main.html', context={'courses': courses})


class CourseView(View):
    def get(self, request, course_id):
        try:
            course = Course.objects.prefetch_related('students').get(id=course_id)
        except Course.DoesNotExist:
            raise Http404
        return render(request, 'course.html', context={'course': course})


class TeacherView(View):
    def get(self, request, teacher_id):
        try:
            teacher = Teacher.objects.get(id=teacher_id)
        except Teacher.DoesNotExist:
            raise Http404
        return render(request, 'teacher.html', context={'teacher': teacher})


class AddCourseView(View):
    def get(self, request):
        form = StudentForm()
        return render(request, 'add_course.html', context={'form': form})

    def post(self, request):
        student = StudentForm(request.POST)

        if student.is_valid():
            student.save()

        return redirect('/schedule/add_course')


class MySignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = '/schedule/main'


class MyLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    redirect_authenticated_user = True