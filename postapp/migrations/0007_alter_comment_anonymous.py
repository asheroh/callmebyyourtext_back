# Generated by Django 4.0.5 on 2023-02-19 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0006_alter_comment_anonymous'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='anonymous',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]