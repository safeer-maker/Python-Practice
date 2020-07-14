import datetime
import time



def log (fun_name = 'None', value = ''):
    log = open('/home/sss/dev/git/Python-Practice/Praticepython.org/file-handling/file.txt', 'a')
    log.write(str(datetime.datetime.now()) + " " + fun_name + " " + str(value) + "\n")
    log.close()


date_time = datetime.datetime.now()
print(date_time)

log ("test time" , 35.22)

