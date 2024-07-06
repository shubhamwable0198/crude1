from django import forms
from . models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

        widgets ={
            'dob': forms.DateInput(attrs={"type": "Date"})
        }

