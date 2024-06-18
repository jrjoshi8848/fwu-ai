from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,logout,login
#from django.contrib.auth import login as lo
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
#from models import CustomUserManager as u
#from django.contrib.auth.models import User
def landing(request):
    return render(request,"home.html")

def log(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            r = user.role
            # Redirect based on user role
            if r.lower()== 'admin':
                return redirect('admin')
            elif r.lower() == 'teacher':
                return redirect('teacher')
            else:
                return redirect('student')
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')

@login_required
def teacher_dashboard(request):
    return render(request,'teacher_dashboard.html')

@login_required
def student_dashboard(request):
    return render(request,'student_dashboard.html')
"""

from atten.acc.models import CustomUserManager

def populate_users():
    for i in range(1, 21):
        uname = f"user{i}"
        passw = f"pass{i}"
        email = f"user{i}@gmail.com"
        
        if i % 3 == 0 and i < 10:
            role = "student"
        elif i % 2 == 0 and i > 10:
            role = "teacher"
        else:
            role = "admin"

        user = CustomUserManager.create_user(
            username=uname,
            email=email,
            password=passw,
            role=role
        )
        print(f"Created user: {uname} with role: {role}")

if __name__ == "__main__":
    populate_users()"""

import os
import django
from django.conf import settings
# Set the settings module
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'atten.settings')
settings.configure(DEBUG=True)
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
django.setup()

settings_module = os.environ.get('DJANGO_SETTINGS_MODULE')

if settings_module:
    print(f"Current DJANGO_SETTINGS_MODULE: {settings_module}")
else:
    print("DJANGO_SETTINGS_MODULE is not set.")