

length_of_array = int(input("Length of input : "))
array = []
output_array = []

for x in range(length_of_array):
    array.append(int(input("Input the number at index " + str(x) +" : ")))
print (array)

for x in range(length_of_array):
        output_array.append(int(length_of_array) - int(x))
        

print (output_array)

output_list = str(output_array)
output = output_list.replace(", ", " ").replace("[","").replace("]",'')
print ("Data in output is " + output)

""" #Hacker rank code but not giving output 

import math
import os
import random
import re
import sys


length_of_array = int(input())
array = []
output_array = []


array.append(input())

for x in range(length_of_array):
        output_array.append(int(length_of_array) - int(x))

out = output_array.replace(", ", " ").replace("[","").replace("]",'')

print (str(output_array))



"""