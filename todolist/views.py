from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
from .models import TodoList
from .models import ToDoObject
# Create your views here.


def homepage(request):
    todolist = TodoList.objects.all()
    context = {"todolists": todolist}
    return render(request, "mytodolist.html", context)


def detail_list(request, id):
    try:
        todolist = TodoList.objects.get(id=id)
        todo_objects = ToDoObject.objects.filter(todolist=todolist)
        context = {'todo_objects': todo_objects}
        return render(request, 'todo_objects.html', context)
    except ObjectDoesNotExist:
        return HttpResponse("Такой страницы не существует", status=404)