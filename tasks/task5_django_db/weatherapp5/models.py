from django.db import models


class Snapshot(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Snapshot {self.id} @ {self.created_at}"


class WeatherRecord(models.Model):
    snapshot = models.ForeignKey(Snapshot, on_delete=models.CASCADE, related_name='records')
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True, null=True)
    temperature_c = models.FloatField(null=True, blank=True)
    humidity_percent = models.FloatField(null=True, blank=True)
    condition = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [models.Index(fields=["city", "created_at"]) ]

    def __str__(self):
        return f"{self.city} {self.temperature_c}C {self.humidity_percent}%"

