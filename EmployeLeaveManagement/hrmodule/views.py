from django.shortcuts import render
from .models import LeaveDetails


# Create your views here.
def viewleaveapplications(request):
    return render(request, 'hrmodule/viewleaveapplications.html')
from employmodule.models import LeaveDetails
def leave_details_list(request):
 leave_details_list = LeaveDetails.objects.all()
 return render(request, 'hrmodule/viewleaveapplications.html',{'leave_details_list': leave_details_list})


