import os
a = 25
a = os.popen('ls ~/temp').read()
a1 = a.split("\n")
print(a1)
