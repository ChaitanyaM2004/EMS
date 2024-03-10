from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('viewleaveapplications',views.viewleaveapplications,name='viewleaveapplications'),
    path('leave_details_list' , views.leave_details_list , name='leave_details_list'),
]