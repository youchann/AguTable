# Generated by Django 2.0.5 on 2018-06-05 23:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='classes',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('weekNum', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)])),
                ('timeNum', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)])),
                ('place', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='table',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('classId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='table.classes')),
            ],
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='table',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='table.user'),
        ),
        migrations.AddField(
            model_name='classes',
            name='teacherId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='table.teacher'),
        ),
    ]
