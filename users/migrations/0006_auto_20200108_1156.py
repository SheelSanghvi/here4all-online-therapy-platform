# Generated by Django 2.2.7 on 2020-01-08 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200108_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answered',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.TextField(default='Reply Pending'),
        ),
    ]
