# Generated by Django 3.2.7 on 2021-09-18 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0007_auto_20210918_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='claimperson',
            name='claim_date',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='claimperson',
            name='claim_object',
            field=models.CharField(default=None, max_length=20),
        ),
    ]