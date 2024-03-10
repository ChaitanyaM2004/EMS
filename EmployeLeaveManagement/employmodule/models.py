from django.db import models

class LeaveDetails(models.Model):
    employee_name = models.CharField(max_length=255)
    leave_type = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()

    def __str__(self):
        return self.employee_name + ' - ' + self.leave_type
