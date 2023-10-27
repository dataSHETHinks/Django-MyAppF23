# Submitted by:
# *--------------------*------------*
# | Krunali Sheth      | 110095010  |
# *--------------------*------------*
# | Srujan Oza         | 110100972  |
# *--------------------*------------*
# | Pratikraj Rajput   | 110097059  |
# *--------------------*------------*
# | Prem Goswami       | 110100984  |
# *--------------------*------------*

from django.db import models


# Create your models here.
class Student(models.Model):
    STUDENT_STATUS_CHOICES = [
        ("ER", "Enrolled"),
        ("SP", "Suspended"),
        ("GD", "Graduated"),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True, default=None)
    date_of_birth = models.DateField()
    status = models.CharField(
        max_length=10, choices=STUDENT_STATUS_CHOICES, default="ER"
    )

    def __str__(self):
        return self.first_name + " " + self.last_name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Instructor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField()
    student = models.ManyToManyField(Student)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Course(models.Model):
    LEVEL_CHOICES = [
        ("BE", "Beginner"),
        ("IN", "Intermediate"),
        ("AD", "Advanced"),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, default=None)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES, default="BE")

    def __str__(self):
        return self.title

class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        (0, 'Order Confirmed'),
        (1, 'Order Cancelled'),
    ]
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    order_status = models.IntegerField(choices=ORDER_STATUS_CHOICES, default=1)
    order_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"Order for {self.student} - {self.course}"