
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('demo-videos/', views.demo_videos, name='demo_videos'),
    path('deployed-projects/', views.deployed_projects, name='deployed_projects'),
]
