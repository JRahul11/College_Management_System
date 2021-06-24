# Generated by Django 3.0.8 on 2021-06-22 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('rno', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmsapp.DepartmentModel')),
            ],
        ),
    ]
