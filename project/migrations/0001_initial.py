# Generated by Django 4.0.4 on 2022-05-11 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0001_initial'),
        ('achievement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tech', models.CharField(max_length=25, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_image', models.ImageField(upload_to='project-image/')),
                ('project_name', models.CharField(max_length=55, unique=True)),
                ('description', models.TextField(max_length=250)),
                ('youtube_link', models.URLField(max_length=150, unique=True)),
                ('github_link', models.URLField(max_length=150, unique=True)),
                ('contributors', models.ManyToManyField(to='member.member')),
                ('hackathon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='achievement.achievement')),
                ('tech', models.ManyToManyField(to='project.tech')),
            ],
        ),
    ]
