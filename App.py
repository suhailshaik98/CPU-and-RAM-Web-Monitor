import csv
import os
import psutil
# from datetime import datetime
import time
import requests

from datetime import datetime,timedelta
import dateutil.parser as dateparser
no_of_cpus= os.cpu_count()
# Getting loadover15 minutes
load1, load5, load15 = psutil.getloadavg()


cpu_usage = (load15/no_of_cpus) * 100
#This function is to get file from the external server
def getfile(url):
  response = requests.get(url+'/'+'memoryasservice.csv')
  response1 = requests.get(url+'/'+'cpuusageservice.csv')
  open('memoryasservice.csv', "wb").write(response.content)
  open('cpuusageservice.csv', "wb").write(response1.content)
# getfile('https://59e9-2603-7080-21f0-9f0-d60d-632d-bc1-de9e.ngrok.io')
def create_data(interval):
  lod = []
  for i in range(0,interval):
      # time_hello=
      new_dict={}
      time.sleep(5)

      # abs_time=abs(time_hello)
      list1=[]
      load1, load5, load15 = psutil.getloadavg()
      cpu_usage = (load15/no_of_cpus) * 100
      list1.append(str(cpu_usage)+" %")
      list1.append(str(psutil.virtual_memory()[2])+" %")
      dt = datetime.now()
    # if str(dt)!=str(datetime.now()):
      time_now=str(dt)[:-7]
      new_dict[time_now]=list1
      lod.append(new_dict)
  return lod
from gpiozero import CPUTemperature
def create_data_forcsv(interval):
  lod = []
  for i in range(0,interval):
      # time_hello=
      new_dict={}
      time.sleep(5)

      # abs_time=abs(time_hello)
      load1, load5, load15 = psutil.getloadavg()
      cpu_usage = (load15/no_of_cpus) * 100
      dt = datetime.now()
    # if str(dt)!=str(datetime.now()):
      time_now=str(dt)[:-7]
      new_dict['Time']=time_now
      new_dict['CPU Usage (%)']=cpu_usage
      new_dict['RAM Usage (%)']=psutil.virtual_memory()[2]
      # new_dict['CPU Temperature']=psutil.sensors_temperatures()
      lod.append(new_dict)
  return lod

def sortedprocessbymem():
  list1=[]
  for i in psutil.process_iter():
    try:
      pidinfo=i.as_dict(attrs=['pid','name','username'])
      pidinfo['vms']=i.memory_info().vms/(2048)
      list1.append(pidinfo)
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
      pass
    list1=sorted(list1,key=lambda procObj:procObj['vms'],reverse=True)
    return list1
  
def readCSV(filename):
  read_list = []
  with open(filename, newline='', encoding="utf-8") as f:
    header = f.readline()
    header = header.strip()
    header_split = header.split(",")
    reader = csv.reader(f)
    for lines in reader:
      read_dict = {}
      for i in range(0, len(header_split)):
        read_dict[header_split[i]] = lines[i]
      read_list.append(read_dict)
    return read_list


def departments(list_of_dictionaries):
  new_list = []
  #list_of_dictionaries=readCSV(filename)
  for i in range(0, len(list_of_dictionaries)):
    for x, y in list_of_dictionaries[i].items():
      if x == 'Name':
        if y in new_list:
          pass
        else:
          new_list.append(y)
  new_list.sort()
  return new_list
def keepOnly(lod, key, values):
  new_lod = []
  for i in range(0, len(lod)):
    if lod[i][key] == values:
      new_lod.append(lod[i])
  return new_lod
def open_hour(dictionary_given):
  for x, y in dictionary_given.items():
    if x == 'Time':
      return y[:-6]
# for i in readCSV('memoryasservice.csv'):
#   print(open_hour(i))
def filterHour(list_of_dictionaries, low, high):
  new_list = []
  for i in range(0, len(list_of_dictionaries)):
#     print(dateparser.parse(open_hour(list_of_dictionaries[i])))
#     print(dateparser.parse(low))
#     print(open_hour(list_of_dictionaries[i]))
    if low <= dateparser.parse(open_hour(list_of_dictionaries[i])) < high:
      new_list.append(list_of_dictionaries[i])
    else:
      pass
  return new_list
#You need to return this function
def data_by_subject(dic):
  print("processing")
  
  date1_hour=dic["hour_start"]
  date2_hour=dic["hour_end"]
  date1=dateparser.parse(date1_hour)
  date2=dateparser.parse(date2_hour)+timedelta(days=1)
#   date2=
  alldate=[]
  # list2=[]
  getdate=[]
  actualdate=[]
  for i in range(0,(date2-date1).days):
    getdate.append(str((date1)+timedelta(days=i))[:-9])
  for i in filepresent:
    if open_hour(i) in alldate:
      continue
    else:
      alldate.append(open_hour(i))
  for i in alldate:
#      print(i[:-3])
     if i[:-3] in getdate:
         actualdate.append(i)
     else:
         continue
#   print(list3)
# print(alldate)
# print(getdate)
  # hello=0
  list1=[]
  list2=[]
  column_counter = -1
  # for i in filepresent:
  #   if open_hour(i) in list1:
  #     continue
  #   else:
  #     list1.append(open_hour(i))
  department_list = departments(filepresent)
#   for i in range(0,len(list1)):
  for depart in department_list:
    d={}
    d['text']=depart
    new_list = []
    column_counter += 1
    department_specific_lod = keepOnly(filepresent, "Name", depart)

    for i in range(0,len(actualdate)):
      hour_specific_lod = filterHour(department_specific_lod, dateparser.parse(actualdate[i]), dateparser.parse(actualdate[i])+timedelta(hours=1))

      new_list.append(countRAM(hour_specific_lod))
    d['x'] = actualdate
    d['y']=new_list
    d['mode']='markers'
    d['marker']={'size':[item * 0.125 for item in new_list]}
    list2.append(d)
  print("done RAM by process")
  return list2   
filepresent=readCSV('memoryasservice.csv')
filepresent1=readCSV('cpuusageservice.csv')
list1=[]

def countRAM(lod):

    TotalRAMUsed=0
    if len(lod)!=0:

        for j in lod:
                TotalRAMUsed+=float(j["RAM Used"])
        return int(round((TotalRAMUsed/len(lod)),2))
    else:
        return 0

def cpuramgraph(dic):
    print("processing cpuramgraph")
    hour_start=dic["hour_start"]
    hour_end=dic["hour_end"]
    lod=keepOnlyhour(filepresent1, 'Time',hour_start,hour_end)    
    #for cpu loop
    cpudicts={
        'type':"scatter",
        'mode':"lines",
        'name':"CPU Usage Percentage",
        'x':open_hour_cpu(lod),
        'y':cpu_values(lod),
    }
    ramdicts={
        'type':"scatter",
        'mode':"lines",
        'name':"RAM Usage Percentage",
        'x':open_hour_cpu(lod),
        'y':ram_values(lod),       
    }    
    list2=[cpudicts,ramdicts]
    return list2
# (psutil.virtual_memory()[0]/(1024*1024))/16
def open_hour_cpu(lod):
 lod2=[]   
 for i in lod:
   for x, y in i.items():
    if x == 'Time' :
         lod2.append(y)
 print("done cpuramgraph")     
 return lod2

def cpu_values(lod):
 list1=[]
 for i in lod:
   for x, y in i.items():
    if x == 'CPU Usage (%)' :
        list1.append(round(float(y),2))
 return list1

def ram_values(lod):
 list1=[]
 for i in lod:
   for x, y in i.items():
    if x == 'RAM Usage (%)' :
        list1.append(round(float(y),2))
 return list1

def keepOnlyhour(lod, key, values_start,values_end):
  new_lod = []
  start=dateparser.parse(values_start)
  end=dateparser.parse(values_end)
  new_values=[]
  for i in range(0,(end-start).days+1):
    new_values.append(str(start+timedelta(days=i)))
  for k in new_values:
      for j in range(0, len(lod)):
        if lod[j][key][:-9] == k[:-9]:
          new_lod.append(lod[j])
#   print(new_values)     
  return new_lod  
# keepOnlyhour(filepresent1,'Time','2022-12-02','2022-12-04')