# Generated by Django 3.1.3 on 2020-11-26 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_auto_20201124_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='question_id',
            field=models.ManyToManyField(blank=True, related_name='tags', to='question.Question'),
        ),
    ]
