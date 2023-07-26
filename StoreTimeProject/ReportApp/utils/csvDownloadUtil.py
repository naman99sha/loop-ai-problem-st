import gdown
import os
from datetime import datetime

# Will download the updated csv from drive to folder in static directory by the name of datetime.utcnow()
# Will return the download location to be used by csvToDbUtil.py
def download_csv(url,filename):
    
    # url = "https://drive.google.com/file/d/1UIx1hVJ7qt_6oQoGZgb8B3P2vd1FD025/view"
    file_id = url.split('/')[-2]

    prefix = 'https://drive.google.com/uc?/export=download&id='
    download_location = "static/" + str(datetime.utcnow())
    os.makedir(download_location)
    gdown.download(prefix+file_id, output=download_location+"/"+filename+".csv")
    return download_location