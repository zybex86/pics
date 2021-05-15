# Generated by Django 3.2.2 on 2021-05-15 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_create_basic_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='plan',
            field=models.ForeignKey(default='B', on_delete=django.db.models.deletion.PROTECT, to='core.plan', verbose_name='plan'),
        ),
    ]
