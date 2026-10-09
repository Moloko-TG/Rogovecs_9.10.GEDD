try:

    SycleRange = int(input("Cik skaitļus jūs gribat ievadīt? "))

    if (SycleRange == 0):
        print("Cikls ir pabeigts, jo skaitlis vienāds 0")

    elif (SycleRange < 0):
        print("Cikls nevar strādat negatīvus reizes")

    else:

        minNumber = 0
        maxNumber = 0

        for i in range(SycleRange):

            UserNumber = int(input("Ievadi savu " + str(i+1) + " skaitli: "))

            if (minNumber > UserNumber or minNumber == 0):
                minNumber = UserNumber

            if (maxNumber < UserNumber or maxNumber == 0):
                maxNumber = UserNumber

        print(f"Mazakais skaitlis: {minNumber}, lielākais skaitlis: {maxNumber}")

except ValueError:

    print("Tas nav skaitlis")
