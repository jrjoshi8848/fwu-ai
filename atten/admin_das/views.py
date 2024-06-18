from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def admin_dashboard(request):
    #print("authentication="+user.is_authenticated+"authentication as admin succesfull\nredrecting to admin")
    return render(request,'admin_dashboard.html')