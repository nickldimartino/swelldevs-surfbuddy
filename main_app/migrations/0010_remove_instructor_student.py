# Generated by Django 5.0.4 on 2024-04-11 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_alter_instructor_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='student',
        ),
    ]
