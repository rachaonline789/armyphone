# Generated by Django 2.2.5 on 2021-05-14 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tb_army_phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('army_name', models.CharField(max_length=100)),
                ('army_rank', models.CharField(max_length=100)),
                ('army_phone', models.CharField(max_length=50)),
                ('army_province', models.CharField(max_length=50)),
                ('army_nickname', models.CharField(max_length=100)),
            ],
        ),
    ]
