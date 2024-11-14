from cmath import sqrt


def startup():
    print ("Would you like to use the calculator?" )
    Sinput = (input()).lower()
    if Sinput in ['yes', 'sure', 'yeah', 'yea', 'y']:
        calc()
    else:
        return[print("Bye Bye")]

def calc():
    a , b = input("\nEnter two values(add space between): ").split() #taking two inputs at one time
    #\n is used to move to new line to make it look cleaner
    print ("First Number: ",a) #Displays first value
    print ("Second Number: ",b) #Displays second value
    a = float(a) #Makes the string into a float
    b = float(b)

    print ("Would you like to add, subtract, multiply, divide, square, or square root? \n")
    Uinput = str(input())
    if Uinput == "add":
        print(a+b)
        restartup()
    elif Uinput == "multiply":
        print(a*b)
        restartup()
    elif Uinput == "subtract":
        print(a-b)
        restartup()
    elif Uinput == "divide":
        print(a/b)
        restartup()
    elif Uinput == "square":
        selection = (input("Which number would you like to square?\nThis can be your first number, second number, both, or the first to the power of the second.\n"))
        if selection in ["both", "first", "first number", "second", "second number", "first to the power of the second"]:
            pass
        else:
            selection = float(selection)
        if selection in [a ,'first', 'first number']:
            print((a)**2)
            restartup()
        elif selection in [b, 'second', 'second number']:
            print((b)**2)
            restartup()
        elif selection in ['both', (a*b)]:
            print((a*b)**2)
            restartup()
        elif selection in ['first to the power of the second', (a)**b]:
            print((a)**b)
            restartup()
    elif Uinput == "square root":
        selection = (input("Which number would you like to square root?\nThis can be your first number, second number, or both.\n"))
        if selection in ["both", "first", "first number", "second", "second number"]:
            pass
        else:
            selection = float(selection)
        if selection in [a ,'first', 'first number']:
            print(sqrt(a))
            restartup()
        elif selection in [b, 'second', 'second number']:
            print(sqrt(b))
            restartup()
        elif selection in ['both', (a*b)]:
            print(sqrt(a*b))
            restartup()
    else:
        print("That function is not available on this calculator, please try again. \n")
        calc()

def restartup():
    print ("Would you like to use the calculator again?" )
    Rinput = (input()).lower()
    if Rinput in ['yes', 'sure', 'yeah', 'yea', 'y']:
        calc()
    else:
        return[print("Bye Bye")]
startup()


