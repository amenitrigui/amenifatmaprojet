# Generated by Django 5.0.6 on 2024-05-19 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(db_column='email', max_length=254, null=True, unique=True),
        ),
    ]
