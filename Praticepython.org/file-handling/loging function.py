import datetime
import time

date_time = datetime.datetime.now()
print(date_time)
log = open('/home/sss/dev/git/Python-Practice/Praticepython.org/file-handling/file.txt', 'a')

for i in range(5):
    log.write(str(datetime.datetime.now()) + "\n")
    i += 1
    time.sleep(1)


log.close()

