# Generated by Django 2.1.1 on 2018-11-10 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_category_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(null=True),
        ),
    ]
