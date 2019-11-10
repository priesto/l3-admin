import psutil
import datetime

date=psutil.boot_time()
d=datetime.datetime.fromtimestamp(date).strftime("%d-%m-%Y %H:%M:%S")
