# Generated by Django 4.2.19 on 2025-02-07 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_parent_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='phone',
            field=models.PositiveBigIntegerField(),
        ),
    ]
