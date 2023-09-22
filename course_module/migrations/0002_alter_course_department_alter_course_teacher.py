# Generated by Django 4.2.5 on 2023-09-17 16:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("department_module", "0001_initial"),
        ("teacher_module", "0001_initial"),
        ("course_module", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="department",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="courses",
                to="department_module.department",
            ),
        ),
        migrations.AlterField(
            model_name="course",
            name="teacher",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="courses",
                to="teacher_module.teacher",
            ),
        ),
    ]