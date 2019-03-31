from django.contrib.auth.models import AbstractUser
from django.db import models

# teams
TECH_TEAM = 'Technical Team'
PARENT_ENGAG_TEAM = 'Parent Engagement Team'
OPS_TEAM = 'Operation Team'
SALES_TEAM = 'Sales Team'
BUSINESS_DEV_TEAM = 'Business Development Team'
CONTENT_TEAM = 'Content Team'
ADMIN = "Administrator"

# creating choices for teams
teams = (
    (ADMIN, "Administrator"),
    (TECH_TEAM, 'Technical Team'),
    (PARENT_ENGAG_TEAM, 'Parent Engagement Team'),
    (OPS_TEAM, 'Operation Team'),
    (SALES_TEAM, 'Sales Team'),
    (BUSINESS_DEV_TEAM, 'Business Development Team'),
    (CONTENT_TEAM, 'Content Team')
)


class CustomUser(AbstractUser):
    role = models.CharField(choices=teams, default='', max_length=30)