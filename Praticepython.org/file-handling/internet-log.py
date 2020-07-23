import os
import datetime
import time

date_time_1 = str(datetime.datetime.now())[:-7]
print(date_time_1)
database_1 = open("database_1" + str(date_time_1[:10]) + ".txt" ,'at')
database_1.write("Date of data " + date_time_1[:10] + "\n")
date_time = date_time_1

while date_time_1[:10] == date_time[:10]:
    a = os.popen("ping -c 1 www.google.com").read()
    b = a.split ('\n')
    c = b[1].split (" ")
    print(b[1])
    print(c)
    date_time = str(datetime.datetime.now())[:-7]
    try:
        if c[3] == "192.168.2.1":
            print ("host not found")
            database_1.write(date_time[12:] + "  " + '0' + "\n")
        else:
            print("Connected to internet")
            database_1.write(date_time[12:] + "  " + '1' + "\n")
    except:
        print("just got Disconnected to internet")
        database_1.write(date_time[12:] + "  " + '0' + "\n")

    time.sleep (1)
else:
    print("procede for shutdown")
    database_1.write("Pi is refreshing at " + date_time + "\n")
    os.system("sudo reboot")
    database_1.close()

