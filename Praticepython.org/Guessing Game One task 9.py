import random

def input_fun():
    while (True):
        user_inp = input("please Enter your hosen number between 1 to 9 : ")
        try:
            user_inp = int(user_inp)
            break
        except:
            print("You have enter an in valid number please try again\n")

    return user_inp


inp = random.randint(1,9)
print("The Rangon no chen is " + str(inp))
user_inp_list = []
while (True):
    user_inp = input_fun()
    user_inp_list.append(user_inp)
    #   print ("User input is " + str(user_inp))
    if user_inp > inp:
        if user_inp > (inp+5):
            print("Too muh greater Guess")
        else:
            print ("Grater value")
    elif user_inp < inp:
        if user_inp < (inp-5):
            print("Too much less Guess")
        else:
            print("Less value")
    else:
        print("This is the guessed number")
        print("Your gusses are " + str(user_inp_list))
        inp_cont = input("Press 1 to continue else close")
        if inp_cont == 1:
            continue
        else:
            break


