from django.db import models
import os
import sys
sys.path.append(os.path.abspath('../students'))
from students.models import Students
from django.utils import timezone


# teams
NONE = 'None'
TECH_TEAM = 'Technical Team'
PARENT_ENGAG_TEAM = 'Parent Engagement Team'
OPS_TEAM = 'Operation Team'
SALES_TEAM = 'Sales Team'
BUSINESS_DEV_TEAM = 'Business Development Team'
CONTENT_TEAM = 'Content Team'

# creating choices for teams
teams = (
    (NONE, 'None'),
    (TECH_TEAM, 'Technical Team'),
    (PARENT_ENGAG_TEAM, 'Parent Engagement Team'),
    (OPS_TEAM, 'Operation Team'),
    (SALES_TEAM, 'Sales Team'),
    (BUSINESS_DEV_TEAM, 'Business Development Team'),
    (CONTENT_TEAM, 'Content Team')
)

# employee status
INTERN = 'Intern'
RETAINER = 'Retainer'
PERMANENT = 'Permanent'

employee_status = (
    (NONE, NONE),
    (INTERN, INTERN),
    (RETAINER, RETAINER),
    (PERMANENT, PERMANENT)
)


# Create your models here.
class Ticket(models.Model):
    students = Students.objects.all()
    students = [(student.student_name, student.student_name) for student in students]
    students = tuple(students)
    OTHER_QUER = 'Other Queries'
    BUG = 'Bug'
    INSTRUC_ISS = 'Instructor Issue'
    PE_ISS = 'PE Issue'
    APP_REL = 'App Related'
    WORK_SKILL_REL = 'Workouts/Skill Related'
    WITHDRAW = 'Withdrawal'
    BATCH_SCHED = 'Batch Scheduling'
    CONT_ISS = 'Content Issue'

    # creating choices for issues
    issues = [
        (OTHER_QUER, 'Other Queries'),
        (BUG, 'Bug'),
        (INSTRUC_ISS, 'Instructor Issue'),
        (PE_ISS, 'PE Issues'),
        (APP_REL, 'App Related'),
        (WORK_SKILL_REL, 'Workouts/Skill Related'),
        (WITHDRAW, 'Withdrawal'),
        (BATCH_SCHED, 'Batch Scheduling'),
        (CONT_ISS, 'Content Issue')
    ]

    concerned_department = models.CharField(choices=teams, default=NONE, max_length=30)
    issue_type = models.CharField(choices=issues, default=OTHER_QUER, max_length=30)
    student_name = models.CharField(choices=students, default="NONE", max_length=30)
    comment = models.TextField(default='', )
    status = models.CharField(max_length=8, editable=False, default='Created')
    opened_by = models.CharField(max_length=50, editable=False, default='None')
    resolution = models.TextField(default='', editable=True, blank=True)
    issued_time = models.DateTimeField(editable=False,
                                       default=timezone.now,
                                       max_length=40)
    resolve_by = models.DateTimeField(editable=False,
                                      default=timezone.now() + timezone.timedelta(days=1))
    resolved_time = models.DateTimeField(editable=True, default=timezone.now)

    def __str__(self):
        return 'Ticket #{}'.format(self.id)


class Employee(models.Model):
    employee_id = models.IntegerField()
    team = models.CharField(choices=teams, default=NONE, max_length=30)
    employee_first_name = models.CharField(max_length=100, default='')
    employee_last_name = models.CharField(max_length=50, default='')
    employee_designation = models.CharField(max_length=50, default='')
    employee_status = models.CharField(choices=employee_status, default=NONE, max_length=30)

    def __str__(self):
        return '{}({})'.format(self.employee_first_name, self.employee_id)



