import random

def input_fun():
    while True:
        guess = input("Enter your choice (1 to 9): ")
        try:
            guess = int(guess)
            if (guess in range(1,9)): raise 'Out of Range:' # this is not working it gernates an error
            break
        except:
            print("Invalid choice")
    return guess


value = random.randint(1,9)
print("The Rangon no chen is " + str(value))
inp_list = []

while (True):
    guess = input_fun()
    inp_list.append(guess)
    #   print ("User input is " + str(guess))
    
    if guess > value:
        if guess > (value+5):
            print("Too much greater Guess")
        else:
            print ("Grater value")
    elif guess < value:
        if guess < (value-5):
            print("Too much less Guess")
        else:
            print("Less value")
    else:
        print("This is the guessed number")
        print("Your gusses are " + str(inp_list))
        inp_cont = input("Press 1 to continue else close")
        
        """
        This should not work:
            You are comparing int with string
            Maybe it will work but try to understand this better
        """

        if inp_cont == '1':
            continue
        else:
            break


