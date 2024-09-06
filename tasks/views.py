from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Employee, Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
    })

def add_task(request):
    if request.method == 'POST':
        task_name = request.POST['task_name']
        employee_name = request.POST['employee_name']
        status = request.POST['status']
        due_date = request.POST['due_date']

        employee, created = Employee.objects.get_or_create(name=employee_name)
        task = Task.objects.create(name=task_name, employee=employee, status=status, due_date=due_date)

        response_data = {
            'id': task.id,
            'name': task.name,
            'employee': task.employee.name,
            'status': task.get_status_display(),
            'due_date': task.due_date
        }

        return JsonResponse(response_data)

def delete_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return JsonResponse({'status': 'success'})
