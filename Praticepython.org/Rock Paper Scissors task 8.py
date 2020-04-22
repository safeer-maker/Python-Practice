
user_1_name = str (input("First user Name : "))
user_2_name = str (input("First user Name : "))

while(True):
    value = [0,0]
    print("Rock Paper Scissors\n1) Rock\n2) Paper\n3) Scissors")
    for i in range (2):
        while (True):
            value[i] = (input("Please Input your seleted value "))
            try:
                value[i] = int(value[i])
                if (int(value[i]) > 0 and int(value[i]) < 4):
                    break
                else:
                    continue
            except:
                continue

    print("Output is " + str(value))

    if (value[0] == value[1]):
        print("It's an tie")
    elif (value[0] == 1 and value[1] == 2):
        print (str(user_1_name) + " Won the match" )
    elif (value[0] == 2 and value[1] == 3):
        print (str(user_1_name) + " Won the match" )
    elif (value[0] == 3 and value[1] == 1):
        print (str(user_2_name) + " Won the match" )
    else:
        print(str(user_2_name) + " Won the match")

    again = input("If u wnat to play again please press 1 else quit : ")
    if(int (again) == 1):
        continue
    else:
        break
