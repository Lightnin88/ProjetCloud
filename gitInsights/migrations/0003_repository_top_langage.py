# Generated by Django 2.0 on 2019-05-16 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gitInsights', '0002_auto_20190405_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='top_langage',
            field=models.TextField(default=None),
        ),
    ]