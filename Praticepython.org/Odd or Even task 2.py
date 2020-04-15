

def odd(data = 0, divider = 2):
    mode = int(data) % int(divider)
    if (int(divider) ==2):
        if (mode == 0):
            print("The number " + str(data) + " is an EVEN number")
        else:
            print("The number " + str(data) + " is an ODD number")
    else:
        if (mode == 0):
            print("The number " + str(data) + " is diviser of " + str(divider))
        else:
            print("The number " + str(data) + " is NOT diviser of " + str(divider))



def inpt():
    data = input("Input Number: ")
    dev = input("Secondary Devider: ")
    ls = [data, dev]
    return ls


inp = list(inpt())
print(inp)
odd(data=inp[0])
odd(inp[0], inp[1])

