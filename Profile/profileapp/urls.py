from django.urls import path
from . import views


urlpatterns =[
    path('', views.index, name='home'),
    path('homepage/', views.homepage, name='homepage'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('delete-account/', views.delete_account, name='delete_account'),
]