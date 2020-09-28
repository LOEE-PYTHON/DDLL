# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20200927_1120'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('u_name', models.CharField(verbose_name='用户名', max_length=10)),
                ('u_pwd', models.CharField(verbose_name='密码', max_length=40)),
                ('u_type', models.IntegerField(verbose_name='用户类型', max_length=1)),
            ],
            options={
                'verbose_name': '用户表',
                'verbose_name_plural': '用户表',
            },
        ),
        migrations.AddField(
            model_name='courseinfo',
            name='c_child_five_theme',
            field=models.CharField(verbose_name='幼儿五大主题', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='coursetypeinfo',
            name='isDelete',
            field=models.BooleanField(verbose_name='是否删除', default=False),
        ),
        migrations.AlterField(
            model_name='courseinfo',
            name='c_mechanical',
            field=models.CharField(verbose_name='机械原理', max_length=1000, null=True),
        ),
    ]
