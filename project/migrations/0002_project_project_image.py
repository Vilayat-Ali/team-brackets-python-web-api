# Generated by Django 4.0.4 on 2022-05-11 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_image',
            field=models.ImageField(default='a', upload_to='project-image/'),
            preserve_default=False,
        ),
    ]
