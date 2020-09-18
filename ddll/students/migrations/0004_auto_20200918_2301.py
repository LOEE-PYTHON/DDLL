# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20200918_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classinfo',
            name='isDelete',
            field=models.BooleanField(verbose_name='是否删除', default=False),
        ),
        migrations.AlterField(
            model_name='courseinfo',
            name='isDelete',
            field=models.BooleanField(verbose_name='是否删除', default=False),
        ),
        migrations.AlterField(
            model_name='moneyinfo',
            name='isDelete',
            field=models.BooleanField(verbose_name='是否删除', default=False),
        ),
        migrations.AlterField(
            model_name='moneyinfo',
            name='m_id',
            field=models.ForeignKey(verbose_name='学生学号', default='', to='students.StudentInfo'),
        ),
        migrations.AlterField(
            model_name='moneyinfo',
            name='m_into_date',
            field=models.DateField(verbose_name='入账时间', default=''),
        ),
        migrations.AlterField(
            model_name='studentclassinfo',
            name='isDelete',
            field=models.BooleanField(verbose_name='是否删除', default=False),
        ),
        migrations.AlterField(
            model_name='studentclassinfo',
            name='sc_bj_id',
            field=models.ForeignKey(verbose_name='上课班级ID', default='', to='students.ClassInfo'),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='isDelete',
            field=models.BooleanField(verbose_name='是否删除', default=False),
        ),
        migrations.AlterField(
            model_name='teacherinfo',
            name='isDelete',
            field=models.BooleanField(verbose_name='是否删除', default=False),
        ),
    ]
