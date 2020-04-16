length_of_array = int(input("Length of input : "))
array = []
output_array = []

for x in range(length_of_array):
    array.append(int(input("Input the number at index " + str(x) +" : ")))
print (array)

for x in range(length_of_array):
        output_array.append(int(length_of_array) - int(x))
        print(x)

print (output_array)

output_list = str(output_array)
output_list.replace(",", " ")
print ("Data in output is " + output_list[1])