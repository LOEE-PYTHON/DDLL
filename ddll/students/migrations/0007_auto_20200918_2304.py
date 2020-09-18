# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_auto_20200918_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moneyinfo',
            name='m_into_date',
            field=models.DateField(verbose_name='入账时间', default='1900-01-01'),
        ),
    ]
