# Generated by Django 4.0.3 on 2022-03-23 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_job_position_user_pay_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]