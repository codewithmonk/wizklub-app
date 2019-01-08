from django.db import models


# Create your models here.
class Instructor(models.Model):
    instructor_name = models.CharField(max_length=100)
    instructor_id = models.IntegerField(unique=True)

    def __str__(self):
        return "{}({})".format(self.instructor_name, self.instructor_id)
