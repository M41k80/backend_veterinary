from django.contrib import admin
from .models import Rating

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('veterinarian', 'pet_owner', 'rating', 'comment', 'timestamp')
    search_fields = ('veterinarian', 'pet_owner', 'rating', 'comment')

