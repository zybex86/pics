# Generated by Django 3.2.2 on 2021-05-15 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.CharField(max_length=1, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
            ],
            options={
                'verbose_name': 'plan type',
                'verbose_name_plural': 'plan types',
                'ordering': ('id',),
            },
        ),
        migrations.AddField(
            model_name='user',
            name='plan',
            field=models.ForeignKey(default='B', on_delete=django.db.models.deletion.PROTECT, to='core.plan', verbose_name='plan'),
            preserve_default=False,
        ),
    ]