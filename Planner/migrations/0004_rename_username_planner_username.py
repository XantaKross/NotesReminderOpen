# Generated by Django 4.1.7 on 2023-04-07 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Planner', '0003_planner_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='planner',
            old_name='username',
            new_name='Username',
        ),
    ]
