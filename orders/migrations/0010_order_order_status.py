# Generated by Django 2.0.7 on 2018-07-28 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20180726_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('INCOMPLETE', 'incomplete'), ('SUBMITTED', 'submitted'), ('FILLED', 'filled')], default='INCOMPLETE', max_length=20),
        ),
    ]
