length_of_array = int(input())
array = []
output_array = []

for x in range(length_of_array):
    array.append(input())
print (array)

for x in range(length_of_array*2-1):
    if x % 2 == 0:
        output_array.append(array[int(length_of_array) - int(x/2)])
        print(x)
    else:
        output_array.append(" ")

print (output_array)