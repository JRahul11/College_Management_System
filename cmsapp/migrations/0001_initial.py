# Generated by Django 3.0.8 on 2021-06-22 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DepartmentModel',
            fields=[
                ('deptid', models.IntegerField(primary_key=True, serialize=False)),
                ('deptname', models.CharField(max_length=20)),
            ],
        ),
    ]