# Generated by Django 3.1.3 on 2020-11-24 08:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='voter',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='voter', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vote',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vote', to=settings.AUTH_USER_MODEL),
        ),
    ]