from django.urls import path
from . import views

app_name = 'myappF23'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('category/<int:category_no>/', views.detail, name='detail'),
    path('instructor/<int:instructor_id>/', views.instructor_courses_students, name='instructor_courses_students'),

]
