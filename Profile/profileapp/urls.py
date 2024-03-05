from django.urls import path
from . import views


urlpatterns =[
    path('', views.index, name='homepage'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('delete-account/', views.delete_account, name='delete_account'),
    path('councilor/', views.councilor, name='councilor'),
    path('oc/', views.oc, name='oc'),
    path('police-service/', views.police_service, name='police_service'),
    path('police-complain/', views.police_complain, name='police_complain'),
    path('police/', views.police, name='police'),
]