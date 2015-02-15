# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('emp_id', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=75)),
                ('ip', models.GenericIPAddressField(protocol=b'IPV4')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('member_id', models.ForeignKey(to='polls.Member')),
                ('question', models.ForeignKey(to='polls.Choice')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
