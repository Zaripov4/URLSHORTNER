# Generated by Django 3.2.9 on 2022-04-04 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LinkInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=10000)),
                ('link_id', models.CharField(max_length=5)),
            ],
        ),
    ]
