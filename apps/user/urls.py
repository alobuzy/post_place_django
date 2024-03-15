from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views._login, name='login'),
    path('logout', views._logout, name='logout'),
    path('<int:id>', views.profile, name='profile'),
    path('', views.profile, name='profile'),
]