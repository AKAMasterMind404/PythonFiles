# Generated by Django 4.0.4 on 2022-05-09 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodelcustom',
            name='age',
            field=models.IntegerField(default=18, null=True),
        ),
        migrations.AlterField(
            model_name='usermodelcustom',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]