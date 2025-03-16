# Generated by Django 5.1.7 on 2025-03-16 19:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0004_projects_module_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_permission',
            name='permission',
        ),
        migrations.AddField(
            model_name='user_permission',
            name='department',
            field=models.ManyToManyField(related_name='user_permission', to='adminapp.department'),
        ),
        migrations.AddField(
            model_name='user_permission',
            name='office',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_permission', to='adminapp.officemodule'),
        ),
        migrations.AddField(
            model_name='user_permission',
            name='project',
            field=models.ManyToManyField(related_name='user_permission', to='adminapp.projects'),
        ),
    ]
