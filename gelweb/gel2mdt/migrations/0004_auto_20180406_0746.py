# Generated by Django 2.0.1 on 2018-04-06 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gel2mdt', '0003_interpretationreportfamilypanel_custom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interpretationreportfamilypanel',
            name='custom',
            field=models.BooleanField(default=False),
        ),
    ]
