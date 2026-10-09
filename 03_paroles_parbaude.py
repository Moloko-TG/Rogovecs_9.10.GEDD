password = "12345678hello"

count = 0

print("Jums ir 3 meģinājumi")
while count < 3:
    userPassword = input("Try to guess the password ")
    if userPassword == password:
        print("Piekļuve atļauta")
        break
    count+=1
    if count < 3:
        print("Jums palika " + str(3-count) + " meģinājumi")
    else:
        print("Piekļuve bloķēta")