# Generated by Django 4.1.3 on 2023-02-26 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('date', models.DateField(blank=True, null=True)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=250)),
                ('number', models.IntegerField()),
                ('mailid', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('department', models.CharField(max_length=250)),
                ('courses', models.CharField(max_length=250)),
                ('purpose', models.CharField(max_length=250)),
                ('materials', models.CharField(max_length=250)),
            ],
        ),
    ]
