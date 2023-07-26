from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(StoreInfo)
admin.site.register(StoreStatusInfo)
admin.site.register(StoreBusinessHours)
admin.site.register(StoreTimezoneData)
admin.site.register(ReportData)