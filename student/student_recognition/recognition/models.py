from django.db import models
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# models.py
from django.db import models

from django.contrib.auth.models import User

# Create a new user


class Faculty(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    faculty_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Store hashed passwords in practice
    terms_accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.faculty_name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    admission_batch = models.IntegerField()  # Year of admission
    academic_performance = models.FloatField()  # GPA or percentage
    consistency = models.FloatField()  # Consistency over semesters
    core_courses_excellence = models.FloatField()  # Performance in core courses
    hackathon_participation = models.IntegerField()  # Number of hackathons attended
    paper_presentations = models.IntegerField()  # Number of research papers presented
    teacher_assistance = models.IntegerField()  # Number of times assisting course teachers

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.admission_batch})"

class StudentRank(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    score = models.FloatField()  # Calculated score based on factors
    rank = models.IntegerField()  # Rank based on score

    def __str__(self):
        return f"{self.student.user.get_full_name()} - Rank: {self.rank}"


class Student_details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Roll_no = models.CharField(max_length=10, unique=True)
    branch = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
