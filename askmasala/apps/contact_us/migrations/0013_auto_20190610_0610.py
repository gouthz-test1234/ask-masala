# Generated by Django 2.2.1 on 2019-06-10 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0012_auto_20190610_0604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
