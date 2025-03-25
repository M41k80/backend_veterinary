from rest_framework import serializers
from .models import MedicalRecord, VaccineRecord, TreatmentRecord


class VaccineRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaccineRecord
        fields = '__all__'


class TreatmentRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreatmentRecord
        fields = '__all__'


class MedicalRecordSerializer(serializers.ModelSerializer):
    vaccines = VaccineRecordSerializer(many=True, read_only=True)
    treatments = TreatmentRecordSerializer(many=True, read_only=True)

    class Meta:
        model = MedicalRecord
        fields = '__all__'
