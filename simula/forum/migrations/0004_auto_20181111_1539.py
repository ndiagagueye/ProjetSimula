# Generated by Django 2.1.1 on 2018-11-11 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20181110_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='update',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
