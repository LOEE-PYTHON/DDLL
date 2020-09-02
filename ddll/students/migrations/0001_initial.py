# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('cl_id', models.CharField(verbose_name='班级ID', max_length=20)),
                ('cl_name', models.CharField(verbose_name='班级名称', max_length=50)),
                ('cl_class_place', models.CharField(verbose_name='上课地点', max_length=100)),
                ('cl_class_data', models.CharField(verbose_name='上课日期', max_length=20)),
                ('cl_class_start_time', models.CharField(verbose_name='上课开始时间', max_length=20)),
                ('cl_class_end_time', models.CharField(verbose_name='上课结束时间', max_length=20)),
                ('cl_note', models.TextField(verbose_name='备注', max_length=1000)),
                ('isDelete', models.BooleanField(verbose_name='逻辑删除', default=0)),
            ],
            options={
                'verbose_name': '班级表',
                'verbose_name_plural': '班级表',
            },
        ),
        migrations.CreateModel(
            name='CourseInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('c_course_id', models.CharField(verbose_name='课程ID', max_length=20, default='')),
                ('c_section_theme', models.CharField(verbose_name='小节主题', max_length=1000)),
                ('c_level', models.CharField(verbose_name='难度', max_length=10)),
                ('c_program_design', models.CharField(verbose_name='程序设计', max_length=1000)),
                ('c_mechanical', models.CharField(verbose_name='物理结构', max_length=1000)),
                ('c_content_theme', models.CharField(verbose_name='内容主题', max_length=20)),
                ('c_scientific', models.CharField(verbose_name='科学原理', max_length=500)),
                ('c_teacher_experience', models.CharField(verbose_name='教学经验', max_length=1000)),
                ('c_course_from', models.CharField(verbose_name='课程来源', max_length=1000)),
                ('isDelete', models.BooleanField(verbose_name='逻辑删除', default=0)),
            ],
            options={
                'verbose_name': '课程详细表',
                'verbose_name_plural': '课程详细表',
            },
        ),
        migrations.CreateModel(
            name='MoneyInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('m_money', models.IntegerField(verbose_name='金额')),
                ('m_into_date', models.DateTimeField(verbose_name='入账时间')),
                ('m_regular_time', models.IntegerField(verbose_name='常规课剩余时间')),
                ('m_special_time', models.IntegerField(verbose_name='特殊课剩余时间')),
                ('m_note', models.TextField(verbose_name='备注', max_length=1000)),
                ('m_discount_from', models.CharField(verbose_name='优惠情况', max_length=500)),
                ('isDelete', models.BooleanField(verbose_name='逻辑删除', default=0)),
            ],
            options={
                'verbose_name': '财务表',
                'verbose_name_plural': '财务表',
            },
        ),
        migrations.CreateModel(
            name='StudentClassInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('sc_section_theme', models.CharField(verbose_name='课程小节主题', max_length=1000)),
                ('sc_date', models.DateField(verbose_name='上课时间')),
                ('sc_use_time', models.IntegerField(verbose_name='所用课时')),
                ('isDelete', models.BooleanField(verbose_name='逻辑删除', default=0)),
                ('kc_id', models.ForeignKey(default='', to='students.CourseInfo')),
                ('sc_bj_id', models.ForeignKey(default='', to='students.ClassInfo')),
            ],
            options={
                'verbose_name': '学生上课表',
                'verbose_name_plural': '学生上课表',
            },
        ),
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('s_name', models.CharField(verbose_name='姓名', max_length=6, default='')),
                ('s_id', models.CharField(verbose_name='学号', max_length=10)),
                ('s_gender', models.BooleanField(verbose_name='性别', default=0)),
                ('s_birthday', models.DateField(verbose_name='出生日期')),
                ('s_phone', models.CharField(verbose_name='手机号码', max_length=20, default='')),
                ('s_status', models.BooleanField(verbose_name='在读状态', default=0)),
                ('s_into', models.DateField(verbose_name='报名日期')),
                ('s_note', models.TextField(verbose_name='备注')),
                ('isDelete', models.BooleanField(verbose_name='逻辑删除', default=0)),
            ],
            options={
                'verbose_name': '学生表',
                'verbose_name_plural': '学生表',
            },
        ),
        migrations.CreateModel(
            name='TeacherInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('t_name', models.CharField(verbose_name='姓名', max_length=10, default=None)),
                ('t_age', models.IntegerField(verbose_name='年龄')),
                ('t_gender', models.BooleanField(verbose_name='性别', default=1)),
                ('t_professional', models.CharField(verbose_name='专业', max_length=100)),
                ('t_school', models.CharField(verbose_name='毕业学校', max_length=200)),
                ('isDelete', models.BooleanField(verbose_name='逻辑删除', default=0)),
            ],
            options={
                'verbose_name': '教师表',
                'verbose_name_plural': '教师表',
            },
        ),
        migrations.AddField(
            model_name='studentclassinfo',
            name='sc_teacher_name',
            field=models.ForeignKey(to='students.TeacherInfo'),
        ),
        migrations.AddField(
            model_name='moneyinfo',
            name='m_id',
            field=models.ForeignKey(default='', to='students.StudentInfo'),
        ),
        migrations.AddField(
            model_name='classinfo',
            name='cl_teacher',
            field=models.ForeignKey(default='', to='students.TeacherInfo'),
        ),
    ]
