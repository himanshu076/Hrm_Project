from django.db import models
from django.utils.translation import gettext_lazy as _


class _It(models.TextChoices):
    BACKEND = 'BE', _('Backend')
    FRONTEND ='FE', _('Frontend')
    QUALITY_ASSURANCE = 'QA', _('Quality Assurance')


class UserDepartment(models.TextChoices):
    ADMIN = 'ADM', _('Admin')
    HUMAN_RESOURCES = 'HR', _('Human Resources')
    ACCOUNT = 'ACCT', _('Account')
    IT = 'It', _('Information Technology')
    BUSINESS_DEVELOPMENT = 'A', _('Business Development')
    MARKETING = 'MKTG', _('Marketing')
    SALES = 'S', _('Sales')

class Gender(models.TextChoices):
    MALE = 'ML', _('Male')
    FEMALE = 'FL', _('Female')
    TRANSGENDER = 'TS', _('Transgender')
    OTHER = 'OT', _('Other')
