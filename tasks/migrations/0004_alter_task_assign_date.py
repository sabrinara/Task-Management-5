# Generated by Django 4.2.7 on 2023-12-29 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_task_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assign_date',
            field=models.DateTimeField(),
        ),
    ]
