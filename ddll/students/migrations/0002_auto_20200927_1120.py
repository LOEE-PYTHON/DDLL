# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassDetailInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('cd_note', models.CharField(verbose_name='备注', max_length=1000, null=True)),
            ],
            options={
                'verbose_name': '学生上课详细表',
                'verbose_name_plural': '学生上课详细表',
            },
        ),
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
                ('cl_note', models.TextField(verbose_name='备注', max_length=1000, null=True)),
                ('isDelete', models.BooleanField(verbose_name='是否删除', default=False)),
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
                ('c_program_design', models.CharField(verbose_name='程序设计', max_length=1000, null=True)),
                ('c_mechanical', models.CharField(verbose_name='物理结构', max_length=1000, null=True)),
                ('c_content_theme', models.CharField(verbose_name='内容主题', max_length=500)),
                ('c_scientific', models.CharField(verbose_name='科学原理', max_length=500, null=True)),
                ('c_teacher_experience', models.CharField(verbose_name='教学经验', max_length=1000, null=True)),
                ('c_classroom', models.CharField(verbose_name='教室', max_length=30)),
                ('c_course_from', models.CharField(verbose_name='课程来源', max_length=1000, null=True)),
                ('isDelete', models.BooleanField(verbose_name='是否删除', default=False)),
            ],
            options={
                'verbose_name': '课程详细表',
                'verbose_name_plural': '课程详细表',
            },
        ),
        migrations.CreateModel(
            name='CourseTypeInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('ct_course_id', models.CharField(verbose_name='课程ID', max_length=20, default='')),
                ('ct_course_name', models.CharField(verbose_name='课程名称', max_length=50, default='')),
                ('ct_study_age', models.CharField(verbose_name='推荐学习年龄', max_length=20, default='')),
                ('ct_equipment', models.CharField(verbose_name='器材', max_length=50, default='')),
                ('ct_note', models.CharField(verbose_name='备注', max_length=2000, default='')),
            ],
            options={
                'verbose_name': '课程总表',
                'verbose_name_plural': '课程总表',
            },
        ),
        migrations.CreateModel(
            name='MoneyInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('m_money', models.IntegerField(verbose_name='金额', default='')),
                ('m_into_date', models.DateField(verbose_name='入账时间', default='1900-01-01')),
                ('m_regular_time', models.IntegerField(verbose_name='购买常规课数量', default='')),
                ('m_special_time', models.IntegerField(verbose_name='购买特殊课数量', null=True, default='')),
                ('m_note', models.TextField(verbose_name='备注', max_length=1000, null=True, default='')),
                ('m_discount_from', models.CharField(verbose_name='优惠情况', max_length=500, null=True)),
                ('isDelete', models.BooleanField(verbose_name='是否删除', default=False)),
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
                ('sc_use_time', models.IntegerField(verbose_name='消耗课时')),
                ('sc_place', models.CharField(verbose_name='上课地点', max_length=50)),
                ('sc_note', models.CharField(verbose_name='备注', max_length=500, null=True)),
                ('isDelete', models.BooleanField(verbose_name='是否删除', default=False)),
                ('sc_bj_id', models.ForeignKey(verbose_name='上课班级ID', null=True, default='', to='students.ClassInfo')),
                ('sc_id', models.ForeignKey(verbose_name='课程ID', default='', to='students.CourseInfo')),
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
                ('s_gender', models.BooleanField(verbose_name='性别', default=False)),
                ('s_birthday', models.DateField(verbose_name='出生日期')),
                ('s_phone', models.CharField(verbose_name='手机号码', max_length=20, default='')),
                ('s_status', models.BooleanField(verbose_name='在读状态', default=True)),
                ('s_into', models.DateField(verbose_name='报名日期')),
                ('s_note', models.TextField(verbose_name='备注', null=True, default='')),
                ('isDelete', models.BooleanField(verbose_name='是否删除', default=False)),
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
                ('t_professional', models.CharField(verbose_name='专业', max_length=100, null=True)),
                ('t_school', models.CharField(verbose_name='毕业学校', max_length=200, null=True)),
                ('t_work_goal', models.CharField(verbose_name='工作方向', max_length=100)),
                ('isDelete', models.BooleanField(verbose_name='是否删除', default=False)),
            ],
            options={
                'verbose_name': '教师表',
                'verbose_name_plural': '教师表',
            },
        ),
        migrations.AddField(
            model_name='studentclassinfo',
            name='sc_teacher_name',
            field=models.ForeignKey(verbose_name='任课老师', to='students.TeacherInfo'),
        ),
        migrations.AddField(
            model_name='moneyinfo',
            name='m_id',
            field=models.ForeignKey(verbose_name='学生学号', default='', to='students.StudentInfo'),
        ),
        migrations.AddField(
            model_name='classinfo',
            name='cl_teacher',
            field=models.ForeignKey(verbose_name='教师姓名', default='', to='students.TeacherInfo'),
        ),
        migrations.AddField(
            model_name='classdetailinfo',
            name='c_id',
            field=models.ForeignKey(verbose_name='课程流水ID', to='students.StudentClassInfo'),
        ),
        migrations.AddField(
            model_name='classdetailinfo',
            name='s_id',
            field=models.ForeignKey(verbose_name='上课学生', to='students.StudentInfo'),
        ),
    ]
