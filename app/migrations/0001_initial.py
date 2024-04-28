# Generated by Django 5.0.3 on 2024-04-22 11:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('deptno', models.IntegerField(max_length=2, primary_key=True, serialize=False)),
                ('dname', models.CharField(max_length=10, unique=True)),
                ('loc', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Salgrade',
            fields=[
                ('grade', models.IntegerField(max_length=4, primary_key=True, serialize=False)),
                ('losal', models.IntegerField(max_length=4)),
                ('hisal', models.IntegerField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('empno', models.IntegerField(max_length=4, primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=10)),
                ('hiredate', models.DateField()),
                ('job', models.CharField(max_length=20)),
                ('sal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('comm', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('deptno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dept')),
                ('mgr', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.emp')),
            ],
        ),
    ]
