# Generated by Django 4.1.5 on 2023-01-03 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0002_alter_about_me_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about_me',
            options={'verbose_name': 'Introduction - About me', 'verbose_name_plural': 'Introduction - About me'},
        ),
    ]
