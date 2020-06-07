# Generated by Django 3.0.6 on 2020-06-07 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resultats', '0007_auto_20200607_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runnerrace',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='resultats.Race', unique=True, verbose_name='Course'),
        ),
        migrations.AlterField(
            model_name='runnerrace',
            name='runner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='resultats.Runner', unique=True, verbose_name='Coureur'),
        ),
        migrations.AlterUniqueTogether(
            name='runnerrace',
            unique_together=set(),
        ),
    ]
