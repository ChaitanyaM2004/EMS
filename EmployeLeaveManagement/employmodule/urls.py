from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
       path('leaveapply/',views.leaveapply,name='leaveapply'),
       path('add_leave_details',views.add_leave_details,name='add_leave_details'),
       path('view_leave_applications',views.view_leave_applications,name='view_leave_applications'),
       path('edit/<int:leave_id>/',views.edit_leave_details,name='edit_leave_details'),
       path('delete/<int:leave_id>/',views.delete_leave_details,name='delete_leave_details'),
]   