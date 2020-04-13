'''
name = str(input ("what {} is your nice name : "))
age = int(input("what is your age: "))
no_of_prints = int(input("How many time do u want to print it : "))

output = ("what At year " + str(99 - age + 2020)+ " your will be at ager 100\n")

print(output * no_of_prints)
'''
'''
import datetime

now = datetime.datetime.now()

name = input("Hey, what's your name?\n")
age = int(input("Okay {}, how old are you?\n".format(name.title())))

yrs = (now.year +100) - age

msg = "Okay {}, so if you're {} now then you should turn 100 in the year {}".format(name.title(),age,yrs)

print(msg)

n = int(input("Okay {}, give me a number\n".format(name)))

print(msg * n)
print("Or does this look nicer?")
msg += "\n"
print(msg * n)
'''
def info(name, age):
    print("Your name " + name.capitalize() + " your age " + age)


def inp_info(name_age):
    name_age.append(str(input("Enter your Nice name: ")))
    #name_age.extend = name
    name_age.append((input("Enter your age: ")))

name_age = list()
inp_info(name_age)
print(name_age)
info(name_age[0], name_age[1])

print("hello Safeer")