# Generated by Django 4.1.2 on 2022-10-04 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Incident_Database', '0003_alter_employees_certificate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='certificate',
            field=models.DecimalField(decimal_places=0, max_digits=7, max_length=30, unique=True, verbose_name='Номер удостоверения'),
        ),
    ]
