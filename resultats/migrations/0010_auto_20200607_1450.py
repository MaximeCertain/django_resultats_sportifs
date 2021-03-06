# Generated by Django 3.0.6 on 2020-06-07 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resultats', '0009_auto_20200607_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runnerrace',
            name='indications',
            field=models.TextField(default='', max_length=100, null=True, verbose_name='Indications spécifiques avant course'),
        ),
        migrations.AlterUniqueTogether(
            name='runnerrace',
            unique_together={('runner', 'race')},
        ),
    ]
