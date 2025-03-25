from django.contrib import admin
from .models import MedicalRecord, VaccineRecord, TreatmentRecord

admin.site.register(MedicalRecord)
admin.site.register(VaccineRecord)
admin.site.register(TreatmentRecord)
