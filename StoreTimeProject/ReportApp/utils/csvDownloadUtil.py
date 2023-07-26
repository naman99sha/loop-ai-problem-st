import gdown
import os
from datetime import datetime

# Will download the updated csv from drive to folder in static directory by the name of datetime.utcnow()
# Will return the download location to be used by csvToDbUtil.py
def download_csv(url):
    
    # url = "https://drive.google.com/file/d/1UIx1hVJ7qt_6oQoGZgb8B3P2vd1FD025/view"
    directoryName = str(datetime.utcnow())
    download_location = "ReportApp/static/" + directoryName
    os.makedirs(download_location)
    retArr = []
    for link in url:
        file_id = link["url"].split('/')[-2]

        prefix = 'https://drive.google.com/uc?/export=download&id='
        gdown.download(prefix+file_id, output=download_location+"/"+link["filename"]+".csv")
        retArr.append(download_location+"/"+link["filename"]+".csv")
    return retArr