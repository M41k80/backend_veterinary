# Generated by Django 5.1.7 on 2025-03-23 01:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(help_text='Content of the message.')),
                ('timestamp', models.DateTimeField(auto_now_add=True, help_text='Timestamp of the message.')),
                ('is_read', models.BooleanField(default=False, help_text='Whether the message has been read or not.')),
                ('receiver', models.ForeignKey(help_text='User that receives the message.', on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(help_text='User that sends the message.', on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
