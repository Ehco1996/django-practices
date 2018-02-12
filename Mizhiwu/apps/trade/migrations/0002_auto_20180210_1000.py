# Generated by Django 2.0.1 on 2018-02-10 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moneycode',
            name='number',
            field=models.DecimalField(blank=True, decimal_places=2, default=10, editable=False, max_digits=10, null=True, verbose_name='捐赠金额'),
        ),
    ]