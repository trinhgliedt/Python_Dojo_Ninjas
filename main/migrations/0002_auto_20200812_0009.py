# Generated by Django 2.2.4 on 2020-08-12 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ninjas',
            new_name='Ninja',
        ),
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.CharField(default='description', max_length=255),
            preserve_default=False,
        ),
    ]
