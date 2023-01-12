#Code for getting dataset for CPU and RAM  usage


import csv
import os
import psutil
from datetime import datetime
import time
no_of_cpus= os.cpu_count()
# Getting loadover15 minutes
l1, l5, l15 = psutil.getloadavg()
def create_data_forcsv():
  lod = []
  for i in range(2):
      # time_hello=
      new_dict={}
      time.sleep(30)

      # abs_time=abs(time_hello)
      l1, l5, l15 = psutil.getloadavg()
      cpu_usage = (l15/no_of_cpus) * 100
      dt = datetime.now()
    # if str(dt)!=str(datetime.now()):
      time_now=str(dt)[:-7]
      new_dict['Time']=time_now
      new_dict['CPU Usage (%)']=cpu_usage
      new_dict['RAM Usage (%)']=psutil.virtual_memory()[2]
      # new_dict['CPU Temperature']=psutil.sensors_temperatures()
      lod.append(new_dict)
  return lod
def writeCSV(name,text):
    if os.path.exists(name):
        write_file = open(name, 'a')
        csv_write = csv.writer(write_file)
        list0=create_data(name,text)
        list1=list0[1:]
    else:
        write_file = open(name, 'w')
        csv_write = csv.writer(write_file)
        list1 = create_data(name,text)
    for i in list1:
        csv_write.writerow(i)
    write_file.close()
def create_data(name,lod):
    list1 = []
    list1.append(list(lod[0].keys()))
    for i in lod:
         list1.append(list(i.values()))

    return list1

# Used this code to run it as a service in Linux Machine

# import signal
# class SignalHandler:
#     shutdown_requested = False

#     def __init__(self):
#         signal.signal(signal.SIGINT, self.request_shutdown)
#         signal.signal(signal.SIGTERM, self.request_shutdown)

#     def request_shutdown(self, *args):
#         print('Request to shutdown received, stopping')
#         self.shutdown_requested = True

#     def can_run(self):
#         return not self.shutdown_requested


# signal_handler=SignalHandler()
# index=0
# while signal_handler.can_run():
      # writeCSV('cpuusageservice.csv',create_data_forcsv())
writeCSV('cpuusageservice.csv',create_data_forcsv())
