# Generated by Django 3.2.19 on 2023-06-22 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppTwo', '0007_auto_20230622_1937'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ApptwoAccessrecord',
        ),
        migrations.DeleteModel(
            name='ApptwoTopic',
        ),
        migrations.DeleteModel(
            name='ApptwoUser',
        ),
        migrations.DeleteModel(
            name='ApptwoWebpage',
        ),
    ]
