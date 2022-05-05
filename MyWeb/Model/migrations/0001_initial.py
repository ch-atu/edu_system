# Generated by Django 3.1.7 on 2022-05-05 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CollegeTable',
            fields=[
                ('college_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('college_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'CollegeTable',
            },
        ),
        migrations.CreateModel(
            name='CourseTable',
            fields=[
                ('course_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=20)),
                ('credit', models.IntegerField(default=4)),
            ],
            options={
                'db_table': 'CourseTable',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=20)),
                ('user_type', models.CharField(default='S', max_length=2)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'User',
            },
        ),
        migrations.CreateModel(
            name='TeacherTable',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Model.user')),
                ('position', models.CharField(max_length=10)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Model.collegetable')),
            ],
            options={
                'db_table': 'TeacherTable',
            },
        ),
        migrations.CreateModel(
            name='StudentTable',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Model.user')),
                ('English_class', models.CharField(max_length=2)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Model.collegetable')),
            ],
            options={
                'db_table': 'StudentTable',
            },
        ),
        migrations.CreateModel(
            name='OpenTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(max_length=20)),
                ('course_time', models.CharField(max_length=20)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Model.coursetable')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Model.teachertable')),
            ],
            options={
                'db_table': 'OpenTable',
                'unique_together': {('course', 'teacher', 'semester')},
            },
        ),
        migrations.CreateModel(
            name='ScoreTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(default=0)),
                ('open', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Model.opentable')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Model.studenttable')),
            ],
            options={
                'db_table': 'ScoreTable',
                'unique_together': {('student', 'open')},
            },
        ),
    ]
