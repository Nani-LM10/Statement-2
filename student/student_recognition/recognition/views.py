from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Student, StudentRank
from sklearn.preprocessing import MinMaxScaler
import numpy as np


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import StudentSignupForm, StudentLoginForm

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentSignupForm



from django.shortcuts import render, redirect
from django.contrib import messages


# views.py
from django.shortcuts import render, redirect
from django.contrib import messages

from django.shortcuts import render, redirect
from .models import Student  # Assuming you have a Student model
from django.contrib import messages  # For displaying success/error messages

def student_reg(request):
    if request.method == 'POST':
        # Get form data
        student_name = request.POST['Student_name']
        roll_no = request.POST['Roll_no']
        branch = request.POST['branch']
        gender = request.POST['gender']
        email = request.POST['email']
        password = request.POST['password']

        # Perform simple validation (you can expand this with custom validation rules)
        if not all([student_name, roll_no, branch, gender, email, password]):
            messages.error(request, "All fields are required.")
            return render(request, 'student_reg.html')

        # Save the data to the database
        student = Student(
            student_name=student_name,
            roll_no=roll_no,
            branch=branch,
            gender=gender,
            email=email,
            password=password  # In production, make sure to hash the password!
        )
        student.save()

        # Redirect to the dashboard or login page after successful signup
        messages.success(request, "Signup successful!")
        return redirect('dashboard')  # Redirect to a dashboard page or login page after signup

    return render(request, 'student_signup.html')


def faculty_registration(request):
    if request.method == 'POST':
        # Here, you can handle the form data
        faculty_name = request.POST.get('faculty_name')
        branch = request.POST.get('branch')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Add your logic for saving the data (e.g., create a Faculty model instance)

        messages.success(request, 'Registration successful!')
        return redirect('faculty_registration')  # Redirect or render a success page

    return render(request, 'faculty_reg.html')



def dash(request):
    return render(request,'dash.html')
# Signup view




     

# Login view
def login_view(request):
    if request.method == 'POST':
        form = StudentLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to homepage after login
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    
    else:
        form = StudentLoginForm()
    
    return render(request, 'login.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')




def Faculty_Reg(request):
    return render(request,'Faculty_Reg.html')
def dashbord(request):
    return render(request,'Dashboard.html')



       

def home(request):
    return render(request,'home.html')

def rank_students(request):
    students = Student.objects.all()
    student_data = []

    # Gather performance data for all students
    for student in students:
        student_data.append([
            student.academic_performance,
            student.consistency,
            student.core_courses_excellence,
            student.hackathon_participation,
            student.paper_presentations,
            student.teacher_assistance
        ])

    # Normalize data for fair comparison
    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(student_data)

    # Calculate the total score for each student
    scores = np.sum(normalized_data, axis=1)
    ranked_students = [(students[i], scores[i]) for i in range(len(students))]
    ranked_students = sorted(ranked_students, key=lambda x: x[1], reverse=True)

    # Update or create the top 3 students' rankings in the database
    StudentRank.objects.all().delete()  # Clear existing rankings
    for i, (student, score) in enumerate(ranked_students[:3]):
        StudentRank.objects.create(
            student=student,
            score=score,
            rank=i + 1
        )

    return render(request, 'rankings.html', {'ranked_students': ranked_students[:3]})

def rankings(request):
    top_students = StudentRank.objects.order_by('rank')  # Get students ordered by rank
    return render(request, 'rankings.html', {'top_students': top_students})
