# models.py

from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    # Add more fields as needed

class WardCouncilor(models.Model):
    name = models.CharField(max_length=100)
    # Add more fields as needed

class PoliceStation(models.Model):
    name = models.CharField(max_length=100)
    # Add more fields as needed

class Criminal(models.Model):
    name = models.CharField(max_length=100)
    # Add more fields as needed
