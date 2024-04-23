# admin.py

from django.contrib import admin
from .models import UserProfile, WardCouncilor, PoliceStation, Criminal

admin.site.register(UserProfile)
admin.site.register(WardCouncilor)
admin.site.register(PoliceStation)
admin.site.register(Criminal)
