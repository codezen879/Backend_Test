# Generated by Django 5.0.3 on 2024-03-24 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_taskcompleted_tcid_alter_taskrejected_trcid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='percentage_Completed',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5),
        ),
    ]
