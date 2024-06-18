from django.contrib import admin
from django.urls import path
from admin_das import views as v0
from acc import views as v1
urlpatterns = [
    path('admin_dashboard/', v0.admin_dashboard, name='admin'),
]