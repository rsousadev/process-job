from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

gender_choices = (
    ('m', 'Male'),
    ('f', 'Female')
)

class Address(models.Model):
    zip = models.IntegerField(blank=True, null=True, validators=[
            MinValueValidator(1)
        ])
    address = models.CharField(max_length=80, blank=False, null=False)
    neighborhood = models.CharField(max_length=80, blank=False, null=False)
    city = models.CharField(max_length=80, blank=False, null=False)
    state = models.CharField(max_length=80, blank=False, null=False)

class Student(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(null=False, blank=False, unique=True)
    enrollment_date = models.DateField(null=False, blank=False)
    school_year = models.IntegerField(null=False, blank=False, validators=[
            MinValueValidator(1)
        ])
    gender = models.CharField(max_length=1, choices=gender_choices)
    birth_date = models.DateField(null=False, blank=False)
    address = models.ManyToManyField(Address)