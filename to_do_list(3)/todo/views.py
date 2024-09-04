from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Todo

@login_required
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})

@login_required
def todo_info(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    return render(request, 'todo/todo_info.html', {'todo': todo})