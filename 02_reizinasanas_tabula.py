try:
    number = int(input("Write positive number: "))
    if (number >= 1):
        for i in range(10):
            print(str(number) + " x " + str((i+1)) + " = " + str(number * (i+1)))
    elif (number == 0):
        print("You can't multiplicate with 0")
    else:
        print("Your wrote negative number")
except ValueError:
    print("It's not number")