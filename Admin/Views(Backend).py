# views.py

from django.shortcuts import render
from .models import UserProfile, WardCouncilor, PoliceStation, Criminal

def admin_panel(request):
    user_profiles = UserProfile.objects.all()
    ward_councilors = WardCouncilor.objects.all()
    police_stations = PoliceStation.objects.all()
    criminals = Criminal.objects.all()
    return render(request, 'admin_panel.html', {
        'user_profiles': user_profiles,
        'ward_councilors': ward_councilors,
        'police_stations': police_stations,
        'criminals': criminals
    })

def delete_user(request, user_id):
    user_profile = UserProfile.objects.get(id=user_id)
    user_profile.delete()
    return redirect('admin_panel')
