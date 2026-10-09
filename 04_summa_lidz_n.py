try:
    number = int(input("Uzraksti veselu pizitīvu skaitļu: "))

    if number < 0:
        print("Skaitlis ir negatīvs")

    elif number == 0:
        print("0 nav pozitīvs skaitlis")

    else:
        EndSum = 0

        for i in range(number):
            EndSum += (i+1)

        print(EndSum)

except ValueError:

    print("Tas nav skaitlis")