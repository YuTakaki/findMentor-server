# Generated by Django 4.0.3 on 2022-04-08 16:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MentorSchedule',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, null=True)),
                ('allDay', models.BooleanField()),
                ('endDate', models.DateTimeField()),
                ('rRule', models.CharField(max_length=100, null=True)),
                ('startDate', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentor_schedule', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]