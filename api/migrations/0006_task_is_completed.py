# Generated by Django 5.0.3 on 2024-03-24 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_task_percentage_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_Completed',
            field=models.BooleanField(default=False),
        ),
    ]