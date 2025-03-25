from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django.utils.dateparse import parse_date
from .models import MedicalRecord
from .serializers import MedicalRecordSerializer
from apps.pets.models import Pet


class MedicalRecordView(ReadOnlyModelViewSet):
    serializer_class = MedicalRecordSerializer

    def get_queryset(self):
        pet_id = self.kwargs.get('pet_id')
        if not pet_id:
            return MedicalRecord.objects.none()

        try:
            pet = Pet.objects.get(id=pet_id)
        except Pet.DoesNotExist:
            raise NotFound("Pet does not exist.")

        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)

        filters = {'pet': pet}
        if start_date:
            filters['appointment__date__gte'] = parse_date(start_date)
        if end_date:
            filters['appointment__date__lte'] = parse_date(end_date)

        return MedicalRecord.objects.filter(**filters).order_by('-appointment__date')

    def retrieve(self, request, *args, **kwargs):
        """ Get a single medical record """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({
            "medical_record": serializer.data,
            "treatments": [
                {"name": t.name, "details": t.details, "start_date": t.start_date}
                for t in instance.treatments.all()
            ],
            "vaccines": [
                {"name": v.name, "applied_date": v.applied_date, "next_dose_date": v.next_dose_date}
                for v in instance.vaccines.all()
            ]
        })
