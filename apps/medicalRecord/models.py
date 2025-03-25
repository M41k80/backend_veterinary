from django.db import models
from django.utils import timezone


class MedicalRecord(models.Model):
    appointment = models.OneToOneField('appointments.Appointment', on_delete=models.CASCADE, related_name='medical_record')
    pet = models.ForeignKey('pets.Pet', on_delete=models.CASCADE, related_name='medical_records')
    veterinarian = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    diagnosis = models.TextField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.pet.name}'s medical record - {self.appointment.date.strftime('%d/%m/%Y')}"


class VaccineRecord(models.Model):
    medical_record = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE, related_name='vaccines')
    name = models.CharField(max_length=255)
    applied_date = models.DateField(default=timezone.now)
    next_dose_date = models.DateField(blank=True, null=True)  # next dose date

    def save(self, *args, **kwargs):
        if not self.next_dose_date:
            self.next_dose_date = self.applied_date.replace(year=self.applied_date.year + 1)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Vaccine {self.name} for {self.medical_record.pet.name}"


class TreatmentRecord(models.Model):
    medical_record = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE, related_name='treatments')
    name = models.CharField(max_length=255)
    details = models.TextField()
    start_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Treatment {self.name} for {self.medical_record.pet.name}"
