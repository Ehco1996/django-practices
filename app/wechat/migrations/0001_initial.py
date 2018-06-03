# Generated by Django 2.0.6 on 2018-06-03 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReplyRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_word', models.CharField(max_length=128, unique=True, verbose_name='关键词')),
                ('content', models.TextField(verbose_name='回复内容')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='添加日期')),
            ],
            options={
                'verbose_name_plural': '自动回复规则',
                'ordering': ('-create_at',),
            },
        ),
        migrations.CreateModel(
            name='UserPic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, max_length=64, verbose_name='用户id')),
                ('media_id', models.CharField(blank=True, max_length=72, verbose_name='图片id')),
                ('image', models.ImageField(upload_to='pics/', verbose_name='图片名字')),
                ('create_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': '用户图片',
                'ordering': ('-create_at',),
            },
        ),
    ]
