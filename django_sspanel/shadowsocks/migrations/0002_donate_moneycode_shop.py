# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-28 12:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shadowsocks.tools


class Migration(migrations.Migration):

    dependencies = [
        ('shadowsocks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='捐赠时间')),
                ('money', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='捐赠金额')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Donate_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MoneyCode',
            fields=[
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='捐赠时间')),
                ('code', models.CharField(blank=True, default=shadowsocks.tools.get_long_random_string, max_length=40, primary_key=True, serialize=False, verbose_name='充值码')),
                ('number', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='捐赠金额')),
                ('isused', models.BooleanField(default=False, verbose_name='是否使用')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Money_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '充值码',
                'ordering': ('-time',),
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='商品描述')),
                ('transfer', models.BigIntegerField(default=1073741824, verbose_name='增加的流量')),
                ('moeny', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='捐赠金额')),
            ],
        ),
    ]