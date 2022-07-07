# Generated by Django 4.0.5 on 2022-07-07 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0001_initial'),
        ('posts', '0004_post_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='topics.topic'),
        ),
    ]
