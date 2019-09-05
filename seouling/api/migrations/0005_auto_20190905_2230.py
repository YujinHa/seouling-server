# Generated by Django 2.1.5 on 2019-09-05 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20190901_2130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='picture',
        ),
        migrations.AlterField(
            model_name='spotpicture',
            name='spot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='api.Spot'),
        ),
    ]
