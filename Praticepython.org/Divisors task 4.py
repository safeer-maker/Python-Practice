
inp = int(input("Please enter the number to find Dividors : "))
rang = range(2,inp)
out = []
for i in range(len(rang)):
    if (inp % rang[i]) == 0:
        out.append(rang[i])

print(out)