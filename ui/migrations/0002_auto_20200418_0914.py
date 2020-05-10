# Generated by Django 2.1.8 on 2020-04-18 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockrank',
            name='amount',
            field=models.CharField(default=100, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stockrank',
            name='high',
            field=models.CharField(default=100, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stockrank',
            name='low',
            field=models.CharField(default=100, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stockrank',
            name='mktcap',
            field=models.CharField(default=100, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stockrank',
            name='nmc',
            field=models.CharField(default=100, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stockrank',
            name='open',
            field=models.CharField(default=100, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stockrank',
            name='pb',
            field=models.CharField(default=100, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stockrank',
            name='per',
            field=models.CharField(default=100, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stockrank',
            name='settlement',
            field=models.CharField(default=100, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stockrank',
            name='turnoverratio',
            field=models.CharField(default=100, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stockrank',
            name='volume',
            field=models.CharField(default=100, max_length=10),
            preserve_default=False,
        ),
    ]
