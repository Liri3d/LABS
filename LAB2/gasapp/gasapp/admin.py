from django.contrib import admin
from .models import GasReading

@admin.register(GasReading)
class GasReadingAdmin(admin.ModelAdmin):
    list_display = ('meter_number', 'reading_date', 'value')
    list_filter = ('meter_number',)
