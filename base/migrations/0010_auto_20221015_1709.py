# Generated by Django 3.2 on 2022-10-15 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_auto_20221015_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilebio',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profilebio',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
