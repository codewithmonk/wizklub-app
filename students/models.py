from django.db import models
import sys
import os
sys.path.append(os.path.abspath('../instructor'))
from instructor.models import Instructor


class Students(models.Model):
    instructor_names = list()
    batches = [(0, "Not assigned"), (1, "Batch 1"), (2, "Batch 2")]
    instructor_names = [(instructor.id, instructor.instructor_name)
                        for instructor in Instructor.objects.all()]
    student_name = models.CharField(max_length=100)
    student_grade = models.CharField(max_length=20)
    mother_email = models.EmailField(blank=True)
    mother_phone_number = models.CharField(max_length=10)
    mother_alternate_phone_number = models.CharField(max_length=10, blank=True)
    father_email = models.EmailField(blank=True)
    father_phone_number = models.CharField(max_length=10)
    father_alternate_phone_number = models.CharField(max_length=10, blank=True)
    apartment = models.CharField(max_length=200)
    apartment_location = models.CharField(max_length=100)
    instructor = models.IntegerField(choices=instructor_names, default=-1)
    batch = models.IntegerField(choices=batches, default=0)

    def __str__(self):
        return "{},({})".format(self.student_name, self.student_grade)
