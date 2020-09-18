# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20200918_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moneyinfo',
            name='m_money',
            field=models.IntegerField(verbose_name='金额', default=''),
        ),
        migrations.AlterField(
            model_name='moneyinfo',
            name='m_note',
            field=models.TextField(verbose_name='备注', max_length=1000, default=''),
        ),
        migrations.AlterField(
            model_name='moneyinfo',
            name='m_regular_time',
            field=models.IntegerField(verbose_name='常规课剩余时间', default=''),
        ),
        migrations.AlterField(
            model_name='moneyinfo',
            name='m_special_time',
            field=models.IntegerField(verbose_name='特殊课剩余时间', default=''),
        ),
    ]
