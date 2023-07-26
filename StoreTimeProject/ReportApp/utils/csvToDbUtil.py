from ReportApp.models import StoreInfo, StoreStatusInfo, StoreBusinessHours, StoreTimezoneData
import csv

def storeStatusInfoUtil(filePath):
    with open(filePath) as file:
        reader = csv.reader(file)
        next(reader)
        
        StoreStatusInfo.objects.all().delete()
        
        for row in reader:
            storeId, _ = StoreInfo.objects.get_or_create(id=row[0])
            storeStatus = StoreStatusInfo(store_id = storeId.id, timestamp_utc = row[2], status = row[1])
            storeStatus.save()
            
def storeBusinessHoursUtil(filePath):
    with open(filePath) as file:
        reader = csv.reader(file)
        next(reader)
        
        StoreBusinessHours.objects.all().delete()
        
        for row in reader:
            storeId, _ = StoreInfo.objects.get_or_create(id=row[0])
            businessHours = StoreBusinessHours(store_id = storeId.id, day = row[1], start_time_local = row[2], end_time_local = row[3])
            businessHours.save()

def storeTimezoneDataUtil(filePath):
    with open(filePath) as file:
        reader = csv.reader(file)
        next(reader)
        
        StoreTimezoneData.objects.all().delete()
        
        for row in reader:
            storeId, _ = StoreInfo.objects.get_or_create(id=row[0])
            if len(row[1]) > 0:
                timezoneData = StoreTimezoneData(store_id = storeId.id, timezone_str = row[1])
            else:
                timezoneData = StoreTimezoneData(store_id = storeId.id)
            timezoneData.save()