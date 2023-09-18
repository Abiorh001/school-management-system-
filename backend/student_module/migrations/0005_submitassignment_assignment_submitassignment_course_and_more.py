# Generated by Django 4.2.5 on 2023-09-18 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("course_module", "0002_alter_course_department_alter_course_teacher"),
        ("teacher_module", "0003_assignment"),
        ("department_module", "0001_initial"),
        ("school_module", "0001_initial"),
        ("student_module", "0004_studentgrade_submitassignment_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="submitassignment",
            name="assignment",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="teacher_module.assignment",
            ),
        ),
        migrations.AddField(
            model_name="submitassignment",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="course_module.course"
            ),
        ),
        migrations.AddField(
            model_name="submitassignment",
            name="department",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="department_module.department",
            ),
        ),
        migrations.AddField(
            model_name="submitassignment",
            name="school",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="school_module.school"
            ),
        ),
        migrations.AddField(
            model_name="submitassignment",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="student_module.student"
            ),
        ),
        migrations.AddField(
            model_name="submitassignment",
            name="teacher",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="teacher_module.teacher"
            ),
        ),
        migrations.AddField(
            model_name="studentgrade",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="course_module.course"
            ),
        ),
        migrations.AddField(
            model_name="studentgrade",
            name="department",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="department_module.department",
            ),
        ),
        migrations.AddField(
            model_name="studentgrade",
            name="school",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="school_module.school"
            ),
        ),
        migrations.AddField(
            model_name="studentgrade",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="student_module.student"
            ),
        ),
        migrations.AddField(
            model_name="studentgrade",
            name="teacher",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="teacher_module.teacher"
            ),
        ),
    ]
