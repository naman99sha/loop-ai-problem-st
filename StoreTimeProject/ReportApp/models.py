from django.db import models
from django.core.validators import MaxValueValidator


# Create your models here.
class StoreInfo(models.Model):
    id = models.BigIntegerField(primary_key=True)
    
    class Meta:
        verbose_name_plural = "Store Info"
    
    def __str__(self):
        return f"Store: {self.id}"
    
class StoreStatusInfo(models.Model):
    status_options = (
        ("active","active"),
        ("inactive","inactive")
    )
    store_id = models.ForeignKey(StoreInfo,on_delete=models.CASCADE,to_field="id", related_name="SSI_store_id", null=True)
    timestamp_utc = models.DateTimeField(null=True)
    status = models.CharField(max_length=250, choices=status_options, null=True)
    
    class Meta:
        verbose_name_plural = "Store Status Info"
    
    def __str__(self):
        return f"{self.store_id.id} - {self.timestamp_utc} - {self.status}"
    
class StoreBusinessHours(models.Model):
    store_id = models.ForeignKey(StoreInfo,on_delete=models.CASCADE,to_field="id", related_name="SBH_store_id", null=True)
    day = models.PositiveIntegerField(validators=[MaxValueValidator(6)], null=True)
    start_time_local = models.TimeField(null=True, blank=True)
    end_time_local = models.TimeField(null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Store Business Hours"

    def __str__(self):
        if self.start_time_local:
            return f"{self.store_id.id} - {self.day}th Day - {self.start_time_local} to {self.end_time_local}"
        else:
            return f"{self.store_id.id} - {self.day}th Day - 24H Open"
        
class StoreTimezoneData(models.Model):
    store_id = models.ForeignKey(StoreInfo,on_delete=models.CASCADE,to_field="id", related_name="STD_store_id", null=True)
    timezone_str = models.CharField(max_length=255, default="America/Chicago")
    
    class Meta:
        verbose_name_plural = "Store Timezone Data"
    
    def __str__(self):
        return f"{self.store_id.id} - {self.timezone_str}"
    
class ReportData(models.Model):
    report_id = models.CharField(max_length=255, primary_key=True)
    store_id = models.ForeignKey(StoreInfo,on_delete=models.CASCADE,to_field="id", related_name="RD_store_id", null=True)
    uptime_last_hour = models.PositiveIntegerField(null=True)
    uptime_last_day = models.PositiveIntegerField(null=True)
    uptime_last_week = models.PositiveIntegerField(null=True)
    downtime_last_hour = models.PositiveIntegerField(null=True)
    downtime_last_day = models.PositiveIntegerField(null=True)
    downtime_last_week = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name_plural = "Report Data"

    def __str__(self):
        return f"{self.store_id.id} Report"