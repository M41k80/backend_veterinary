# Generated by Django 5.1.7 on 2025-03-24 21:57

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appointments', '0004_appointment_end_time_appointment_start_time_and_more'),
        ('pets', '0003_alter_pet_pet_owner'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosis', models.TextField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('appointment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='medical_record', to='appointments.appointment')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medical_records', to='pets.pet')),
                ('veterinarian', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TreatmentRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('details', models.TextField()),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('medical_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='treatments', to='medicalRecord.medicalrecord')),
            ],
        ),
        migrations.CreateModel(
            name='VaccineRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('applied_date', models.DateField(default=django.utils.timezone.now)),
                ('next_dose_date', models.DateField(blank=True, null=True)),
                ('medical_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vaccines', to='medicalRecord.medicalrecord')),
            ],
        ),
    ]
