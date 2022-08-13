# Generated by Django 4.1 on 2022-08-13 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='todo_objects',
        ),
        migrations.AddField(
            model_name='todoobject',
            name='todolist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='todolist', to='todolist.todolist'),
        ),
    ]