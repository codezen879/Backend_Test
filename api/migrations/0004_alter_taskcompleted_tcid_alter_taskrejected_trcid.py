# Generated by Django 5.0.3 on 2024-03-21 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_delete_tasks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskcompleted',
            name='tcid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='taskrejected',
            name='trcid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
