# Generated by Django 4.0.5 on 2022-06-21 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gasstation',
            name='id',
        ),
        migrations.AddField(
            model_name='gasstation',
            name='_id',
            field=models.CharField(default='', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='gasstation',
            name='date_insert',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gasstation',
            name='dieasel',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='gasstation',
            name='fechaaplicacion',
            field=models.CharField(max_length=255),
        ),
    ]