from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Student

# Signup form
class StudentSignupForm(UserCreationForm):
    roll_no = forms.CharField(max_length=10, required=True)
    branch = forms.CharField(max_length=100, required=True)
    gender = forms.CharField(max_length=10, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            student = Student(user=user, roll_no=self.cleaned_data['roll_no'], branch=self.cleaned_data['branch'], gender=self.cleaned_data['gender'])
            student.save()
        return user


# Login form (optional, you can use Django's built-in AuthenticationForm directly)
class StudentLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
