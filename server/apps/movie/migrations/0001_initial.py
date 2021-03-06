# Generated by Django 2.1.4 on 2019-04-22 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='演员名称')),
            ],
            options={
                'verbose_name': ('演员',),
                'verbose_name_plural': ('演员',),
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=30, verbose_name='电影类型')),
            ],
            options={
                'verbose_name': '电影类型',
                'verbose_name_plural': '电影类型',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='电影标题')),
                ('doubanId', models.CharField(blank=True, max_length=20, null=True, verbose_name='豆瓣id')),
            ],
            options={
                'verbose_name': '电影信息',
                'verbose_name_plural': '电影信息',
            },
        ),
    ]
