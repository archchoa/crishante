# Generated by Django 2.1.2 on 2018-10-31 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='work',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
