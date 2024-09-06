from django import forms
from .models import Employee, Task

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Employee Name'}),
        }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'employee', 'status', 'due_date']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Task Name'}),
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }
