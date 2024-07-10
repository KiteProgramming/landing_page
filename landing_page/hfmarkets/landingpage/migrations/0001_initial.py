# Generated by Django 5.0.4 on 2024-04-05 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TblUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('country_code', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
    ]
