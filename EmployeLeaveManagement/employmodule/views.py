from django.shortcuts import get_object_or_404, render,redirect


from .models import LeaveDetails  # Import the LeaveDetails model

def leaveapply(request):
    return render(request, 'employmodule/leaveapply.html')

def add_leave_details(request):
    if request.method == 'POST':
        employee_name = request.POST.get('employename')
        leave_type = request.POST.get('leave_type')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        reason = request.POST.get('reason')

        leave_details = LeaveDetails(
            employee_name=employee_name,
            leave_type=leave_type,
            start_date=start_date,
            end_date=end_date,
            reason=reason,

        )
        leave_details.save()  # Corrected save method
        return render(request, 'employmodule/datainserted.html')
    return render(request, 'employhomepage.html')

def view_leave_applications(request):
    leave_details_list = LeaveDetails.objects.all()  # Corrected variable name
    return render(request, 'employmodule/view_leave_applications.html', {'leave_details_list': leave_details_list})

def edit_leave_details(request, leave_id):
    if not request.user.is_authenticated:
        return redirect("login")
    
    leave = LeaveDetails.objects.get(id=leave_id)
    
    if request.method == 'POST':
        employee_name = request.POST['employee_name']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        leave_type = request.POST['leave_type']
        reason = request.POST['reason']
        

        leave.employee_name = employee_name
        leave.leave_type = leave_type
        leave.reason = reason
        

        if start_date:
            leave.start_date = start_date
        if end_date:
            leave.end_date = end_date

        leave.save()
        alert = True
        return render(request, 'employmodule/edit_leave_details.html', {'alert': alert})

    return render(request, 'employmodule/edit_leave_details.html', {'leave_details': leave })

def delete_leave_details(request, leave_id):
    leave_details = get_object_or_404(LeaveDetails, id=leave_id)
    if request.method == 'POST':
        leave_details.delete()
        return redirect("employhomepage")
    return render(request, 'employmodule/delete_leave_details.html', {'leave_details': leave_details})
        
    