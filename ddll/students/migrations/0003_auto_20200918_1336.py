# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20200918_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classinfo',
            name='cl_teacher',
            field=models.ForeignKey(verbose_name='教师姓名', default='', to='students.TeacherInfo'),
        ),
        migrations.AlterField(
            model_name='studentclassinfo',
            name='kc_id',
            field=models.ForeignKey(verbose_name='课程ID', default='', to='students.CourseInfo'),
        ),
        migrations.AlterField(
            model_name='studentclassinfo',
            name='sc_teacher_name',
            field=models.ForeignKey(verbose_name='教师姓名', to='students.TeacherInfo'),
        ),
    ]
