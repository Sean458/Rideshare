# Generated by Django 3.1.2 on 2020-10-09 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='cost',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='seats',
            field=models.IntegerField(),
        ),
    ]
