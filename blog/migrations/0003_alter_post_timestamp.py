# Generated by Django 5.2.4 on 2025-07-23 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_contact_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timeStamp',
            field=models.DateTimeField(blank=True),
        ),
    ]
