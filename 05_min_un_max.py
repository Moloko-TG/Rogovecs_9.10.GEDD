try:

    SycleRange = int(input("Cik skaitļus jūs gribat ievadīt? "))

    if (SycleRange == 0):
        print("Cikls ir pabeigts, jo skaitlis vienāds 0")

    elif (SycleRange < 0):
        print("Cikls nevar strādat negatīvus reizes")

    else:

        minNumber = None
        maxNumber = None

        for i in range(SycleRange):

            UserNumber = int(input("Ievadi savu " + str(i+1) + " skaitli: "))

            if (minNumber == None or minNumber > UserNumber):
                minNumber = UserNumber

            if (maxNumber == None or maxNumber < UserNumber):
                maxNumber = UserNumber

        print(f"Mazakais skaitlis: {minNumber}, lielākais skaitlis: {maxNumber}")

except ValueError:

    print("Tas nav skaitlis")
