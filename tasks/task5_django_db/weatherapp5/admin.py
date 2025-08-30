from django.contrib import admin
from .models import Snapshot, WeatherRecord


@admin.register(Snapshot)
class SnapshotAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at")
    ordering = ("-created_at",)


@admin.register(WeatherRecord)
class WeatherRecordAdmin(admin.ModelAdmin):
    list_display = ("id", "snapshot", "city", "temperature_c", "humidity_percent", "created_at")
    list_filter = ("city",)
    search_fields = ("city",)
    ordering = ("-created_at",)

