from django.db import models

# Create your models here.


class TodoList(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ToDoObject(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    deadline = models.DateTimeField()
    done = models.BooleanField()
    todolist = models.ForeignKey(to=TodoList, null=True, on_delete=models.SET_NULL,
                                     related_name='todolist')
    objects = models.Manager()


    def __str__(self):
        return self.name

