"""import os
import django
from django.conf import settings
#from django.contrib.auth.models import User
#from accounts.models import CustomUserManager
# Set up Django's settings module manually
#settings.configure()
os.environ.setdefault('DJANGO_SETTING_MODULE','atten.settings')
settings.configure(DEBUG=True)
django.setup()
from acc.models import CustomUserManager as U
num_records = 20

# Generate and insert data
for i in range(1, num_records + 1):
    uname = f"user{i}"
    passw= f"pass{i}"
    email=f"user"+str(i)+"@gmail.com"
    
    if i % 3 == 0 and i < 10:
        r="student"
    elif i % 2 == 0 and i > 10:
        r="teacher"
    else:
        r="admin"
    user = U.object.create_user(
        username=uname,
        email=email,
        password=passw,
        role = r
    )
    print(f"Created user: {user.username} with role: {user.role}")"""


# scripts/create_users.py
# accounts/pop.py
"""import os
import django
from django.conf import settings
# Set the settings module
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'atten.settings')
settings.configure(DEBUG=True)
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
django.setup()

from .models import CustomUserManager

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

# Get the current value of DJANGO_SETTINGS_MODULE
import django
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
# Set the path to your Django project's settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE','atten.settings')

# Now you can setup Django
django.setup()

settings_module = os.environ.get('DJANGO_SETTINGS_MODULE')

if settings_module:
    print(f"Current DJANGO_SETTINGS_MODULE: {settings_module}")
else:
    print("DJANGO_SETTINGS_MODULE is not set.")