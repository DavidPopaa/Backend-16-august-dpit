# Generated by Django 4.0.6 on 2022-08-11 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DetailsModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dist1', models.CharField(max_length=100)),
                ('dist2', models.CharField(max_length=100)),
                ('dist3', models.CharField(max_length=100)),
                ('dist4', models.CharField(max_length=100)),
            ],
        ),
    ]