from django.urls import path

from . import views

urlpatterns =[
    path('', views.search, name='search'),
    path('<int:id>', views.detail, name='detail'),
    path('create', views.create, name='create'),
]