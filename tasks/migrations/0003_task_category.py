# Generated by Django 4.2.7 on 2023-12-29 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_remove_category_task'),
        ('tasks', '0002_remove_task_category_remove_task_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.ManyToManyField(to='categories.category'),
        ),
    ]
