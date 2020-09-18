# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moneyinfo',
            name='m_id',
            field=models.ForeignKey(verbose_name='财务ID', default='', to='students.StudentInfo'),
        ),
        migrations.AlterField(
            model_name='moneyinfo',
            name='m_into_date',
            field=models.DateField(verbose_name='入账时间'),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='s_status',
            field=models.BooleanField(verbose_name='在读状态', default=True),
        ),
    ]
