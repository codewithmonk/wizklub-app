from django.shortcuts import render
from .models import Instructor


# Create your views here.
def post_instructor_list(request):
    instructors = Instructor.objects.all()
    return render(request, 'instructor/post_instructor_list.html', {'instructors': instructors})
