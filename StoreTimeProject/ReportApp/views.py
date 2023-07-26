from django.shortcuts import render, HttpResponse
from .models import *
from .utils import csvDownloadUtil

# Create your views here.
def home(request):
    urlArr = [
        {"url": "https://drive.google.com/file/d/1UIx1hVJ7qt_6oQoGZgb8B3P2vd1FD025/view","filename": "store_status"},
        {"url": "https://drive.google.com/file/d/101P9quxHoMZMZCVWQ5o-shonk2lgK1-o/view", "filename": "store_timezone"},
        {"url": "https://drive.google.com/file/d/1va1X3ydSh-0Rt1hsy2QSnHRA4w57PcXg/view", "filename": "store_business_hours"}
    ]
    [storeStatusFilename, storeTimezoneFilename, storeBusinessHoursFilename] = csvDownloadUtil.download_csv(urlArr)
    print("---------"+storeStatusFilename)
    return HttpResponse("Done")