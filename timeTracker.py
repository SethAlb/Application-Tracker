import psutil 
import win32process, win32gui 
import time 
import csv 
from datetime import date

csv_file = "TaskTracker.csv"
process_name = ""
date = date.today()
start = time.time()
while True:
        
        hwnd = win32gui.GetForegroundWindow()
        _,pid = win32process.GetWindowThreadProcessId(hwnd)
        process = psutil.Process(pid)     
        if process_name != process.name(): 

            end = time.time()
            TotalTime= (end-start)/60
            print (process_name, TotalTime)
            if process_name != "": 
                with open(csv_file, mode='a', newline='') as file: 
                    writer=csv.writer(file)
                    writer.writerow([process_name,"%.2f" % round(TotalTime, 2),date])
            process_name = process.name() 
            start = time.time()

        time.sleep(1)




    

