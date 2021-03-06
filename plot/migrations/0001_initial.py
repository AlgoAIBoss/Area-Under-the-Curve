# Generated by Django 3.2.9 on 2021-11-17 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Methods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Plot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('function', models.CharField(max_length=100)),
                ('start', models.IntegerField()),
                ('end', models.IntegerField()),
                ('split', models.IntegerField()),
                ('method', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='plot.methods')),
            ],
        ),
    ]
