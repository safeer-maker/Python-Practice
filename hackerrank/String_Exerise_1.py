'''
data = "Welcome to Python 101:Strings"

low_str = data.lower()
print(low_str)

outstr = low_str[0:7]+" " + low_str[-5:-1]+" " + low_str[8:10]+" " + low_str[13] + low_str[12] + low_str[2] + low_str[1] + low_str[-5]

print(outstr.title())

print(outstr[::-1])
'''

sam = [1, 99, 6, 33]
sam1 = [i * 2 for i in sam]
sam.sort()
sam1
print(str(sum(sam)))
