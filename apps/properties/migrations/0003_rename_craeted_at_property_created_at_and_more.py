# Generated by Django 4.0 on 2022-02-06 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='craeted_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='propertyviews',
            old_name='update_at',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='property',
            name='update_at',
        ),
        migrations.RemoveField(
            model_name='propertyviews',
            name='craeted_at',
        ),
        migrations.AddField(
            model_name='property',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='propertyviews',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
