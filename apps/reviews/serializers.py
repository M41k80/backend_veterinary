from rest_framework import serializers
from .models import Rating

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'veterinarian', 'pet_owner', 'appointment', 'rating', 'comment', 'timestamp']
        read_only_fields = ['timestamp']
