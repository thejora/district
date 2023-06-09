# Generated by Django 4.1.2 on 2023-04-04 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('district_2308', models.CharField(blank=True, max_length=10)),
                ('district_2309', models.CharField(blank=True, max_length=10)),
                ('district_2310', models.CharField(blank=True, max_length=10)),
                ('district_2311', models.CharField(blank=True, max_length=10)),
                ('district_2312', models.CharField(blank=True, max_length=10)),
                ('remark', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
