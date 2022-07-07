# Generated by Django 4.0.5 on 2022-07-07 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0001_initial'),
        ('posts', '0003_remove_post_topic_alter_post_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Topic',
            field=models.ForeignKey(blank=True, default=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='topics.topic'),
        ),
    ]
