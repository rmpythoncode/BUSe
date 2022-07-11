# Generated by Django 2.2.3 on 2019-08-02 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bdata', '0007_auto_20190802_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bpoint',
            name='route',
            field=models.ManyToManyField(related_name='route', to='bdata.Route'),
        ),
        migrations.AlterField(
            model_name='bus',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buses', to='bdata.Route'),
        ),
    ]