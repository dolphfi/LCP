from django.urls import path
from . import views

urlpatterns = [
    path('lncp_members/', views.index, name='index'),
    path('lncp_members/index', views.index, name='index'),
    path('lncp_members/about', views.about, name='about_us'),
    path('lncp_members/services', views.services, name='our-services'),
    path('lncp_members/contact', views.contact, name='contact_us'),
     
     
]