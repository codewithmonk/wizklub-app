from django.shortcuts import render
from .models import Students


# Create your views here.
def search_student(request, id):
    student = Students.objects.get(id=id)
    return render(request, "student_search.html", {'student': student})



