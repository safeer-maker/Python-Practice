import  os

a = os.popen("iwconfig").read()
b = a.split("ESSID")[1]
print (b)
c = b.split('"')
print (c)