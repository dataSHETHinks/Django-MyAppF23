from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponse
from .models import Category, Course, Instructor


def index(request):
    category_list = Category.objects.all().order_by('id')[:10]
    course_list = Course.objects.all().order_by('-price')[:5]
    professor_list = Instructor.objects.all().order_by('last_name')
    context = {
        'category_list': category_list,
        'course_list': course_list,
        'professor_list': professor_list,
    }
    return render(request, 'myappF23/index.html', context)


def about(request):
    return render(request, 'myappF23/about.html')


def detail(request, category_no):
    category = get_object_or_404(Category, pk=category_no)
    course_list = Course.objects.filter(categories=category)
    return render(request, 'myappF23/detail.html', {'category': category, 'course_list': course_list})


def instructor_courses_students(request, instructor_id):
    instructor = get_object_or_404(Instructor, pk=instructor_id)
    courses = Course.objects.filter(instructor=instructor)

    context = {
        'instructor': instructor,
        'courses': courses,
    }
    return render(request, 'myappF23/instructor_detail.html', context)
