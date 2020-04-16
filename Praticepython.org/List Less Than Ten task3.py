
def less_then(a, const = 5):
    less_list = []
    for i in range(len(a)):
        if int(a[i]) < const:
            less_list.append(a[i])
    return less_list


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in range(len(a)):
    if int(a[i]) < 5:
        print (a[i])

print(less_then(a))
const = int(input("please input the number: "))
print(less_then(a,const))
