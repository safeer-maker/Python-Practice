
inp = str(input("Enter the line "))

for i in range(len(inp)):
    if inp[i] == inp[len(inp) -1 -i]:
        continue
    else:
        print("This is not palindrome ")
        break
    print("string is palindrome")        # this string is not appering in the code

