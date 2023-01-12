#Code for getting dataset for RAM per process usage
import csv
import os
import psutil
from datetime import datetime
import time
def sortedprocessbymem():
  list1=[]
  for i in psutil.process_iter():
    try:
      pidinfo=i.as_dict(attrs=['pid','name'])
      pidinfo['rss']=i.memory_info().rss/(1024*1024)
      list1.append(pidinfo);
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
      pass
  list1=sorted(list1,key=lambda procObj:procObj['rss'],reverse=True)
  return list1

def getlodmem(numberofprograms):
    listOfRunningProcess = sortedprocessbymem()
    list2=[]
    for elem in listOfRunningProcess[:numberofprograms] :
        dt = datetime.now()
    # if str(dt)!=str(datetime.now()):
        time_now=str(dt)[:-7]
        elem['Time']=time_now
        elem['PID']=elem['pid']
        del elem['pid']
        elem['Name']=elem['name']
        del elem['name']
        elem['RAM Used']=elem['rss']
        del elem['rss']
        list2.append(elem)


    return list2
def findprogramname(programname):
    sortedprocess=sortedprocessbymem()
    for i in sortedprocess:
        if i['name']==programname:
            return i
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
#         writeCSV('/home/charan/memoryasservice.csv',getlodmem(10))
#         time.sleep(30)
writeCSV('memoryasservice.csv',getlodmem(10))
