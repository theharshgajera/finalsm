# Generated by Django 5.2 on 2025-04-24 17:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0029_studentresult"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="staff_leave",
            name="data",
        ),
        migrations.RemoveField(
            model_name="student_leave",
            name="data",
        ),
        migrations.RemoveField(
            model_name="subject",
            name="staff",
        ),
        migrations.AddField(
            model_name="attendance_report",
            name="status",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="staff",
            name="subjects",
            field=models.ManyToManyField(
                blank=True, related_name="staff_members", to="app.subject"
            ),
        ),
        migrations.AddField(
            model_name="staff_leave",
            name="date",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="student_leave",
            name="date",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="studentresult",
            name="attendance_mark",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="studentresult",
            name="end_sem_mark",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="studentresult",
            name="ia1_mark",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="studentresult",
            name="ia2_mark",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="studentresult",
            name="midsem_mark",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="attendance",
            name="session_year_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.session_year"
            ),
        ),
        migrations.AlterField(
            model_name="attendance",
            name="subject_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.subject"
            ),
        ),
        migrations.AlterField(
            model_name="attendance_report",
            name="student_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.student"
            ),
        ),
        migrations.AlterField(
            model_name="staff_feedback",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="staff_leave",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="student",
            name="course_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.course"
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="session_year_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.session_year"
            ),
        ),
        migrations.AlterField(
            model_name="student_feedback",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="student_leave",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="studentresult",
            name="assignment_mark",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="studentresult",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="studentresult",
            name="exam_mark",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="studentresult",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
