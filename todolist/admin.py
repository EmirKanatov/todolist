from django.contrib import admin
from .models import TodoList, ToDoObject
# Register your models here.

admin.site.register(TodoList)
admin.site.register(ToDoObject)
