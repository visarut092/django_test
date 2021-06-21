# Generated by Django 3.2.4 on 2021-06-21 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=5)),
                ('specie', models.CharField(max_length=100)),
                ('weight', models.CharField(max_length=10)),
                ('blood_type', models.CharField(max_length=10)),
            ],
        ),
    ]
