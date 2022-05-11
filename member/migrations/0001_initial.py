# Generated by Django 4.0.4 on 2022-05-11 11:41

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='memberRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='memberSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='member-image/')),
                ('name', models.CharField(max_length=25)),
                ('nationality', django_countries.fields.CountryField(max_length=2)),
                ('about', models.TextField(max_length=150)),
                ('github_url', models.CharField(max_length=125, unique=True)),
                ('role', models.ManyToManyField(to='member.memberrole')),
                ('skill', models.ManyToManyField(to='member.memberskill')),
            ],
            options={
                'ordering': ['name', 'github_url'],
            },
        ),
    ]
