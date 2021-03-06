# Generated by Django 3.1.3 on 2020-11-30 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_userprofile_user_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='about_yourself',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='place_of_employment',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
