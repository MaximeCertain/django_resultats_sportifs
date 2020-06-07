# Generated by Django 3.0.6 on 2020-06-07 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resultats', '0005_auto_20200607_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='runnerrace',
            name='bibNumber',
            field=models.FloatField(default=0, verbose_name='Numéro de dossard du coureur'),
        ),
        migrations.AlterField(
            model_name='runnerrace',
            name='indications',
            field=models.TextField(max_length=100, null=True, verbose_name='Indications spécifique du médécin'),
        ),
        migrations.AlterField(
            model_name='runnerrace',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='resultats.Race', verbose_name='Course'),
        ),
        migrations.AlterField(
            model_name='runnerrace',
            name='runner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='resultats.Runner', verbose_name='Coureur'),
        ),
    ]