# Generated by Django 4.1.7 on 2023-03-12 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gres', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livres',
            name='identifiant',
            field=models.IntegerField(default=0, editable=False, primary_key=True, serialize=False),
        ),
    ]
