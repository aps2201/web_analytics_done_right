# Generated by Django 2.2.1 on 2020-03-25 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curvit', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='general',
            options={'verbose_name_plural': 'CV Main'},
        ),
        migrations.RemoveField(
            model_name='general',
            name='certification',
        ),
        migrations.RemoveField(
            model_name='general',
            name='education',
        ),
        migrations.RemoveField(
            model_name='general',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='general',
            name='volunteering',
        ),
    ]