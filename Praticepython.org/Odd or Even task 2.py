
def odd(data = 0, divider = 2):
    print("sam")
    print(data)


def inpt():
    data = input("Input Number: ")
    dev = input("Secondary Devider: ")
    ls = [data, dev]
    return ls


inp = list(inpt())
print(inp)
odd(data=inp[0])



