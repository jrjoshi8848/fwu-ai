from django.contrib import admin
from django.urls import path,include
from acc import views as v0
from admin_das import views as v1
urlpatterns = [
    path('', v0.landing,name='landing'),
    path('log/', v0.log,name='login'),
    path('logout/', v0.user_logout, name='logout'),
    path('admin_dashboard/', v1.admin_dashboard, name='admin'),
    path('staff_dashboard/', v0.teacher_dashboard, name='teacher'),
    path('user_dashboard/', v0.student_dashboard, name='student'),
    #path('validate/', views.log, name='validate'),

]