from django.shortcuts import render, get_object_or_404
from .models import Department

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department_list.html', {'departments': departments})

def department_detail(request, slug):
    department = get_object_or_404(Department, slug=slug)
    return render(request, 'department_detail.html', {'department': department})
