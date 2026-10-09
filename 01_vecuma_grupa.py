age = input("Write your age: ")
try:
    age = int(age)
    if age == '' or age < 0:
        age = 0
except ValueError:
    print("It's not an age")


if age <= 10:
    print('bērns')
elif age <= 20:
    print('pusaudzis')
elif age <= 38:
    print('pieaugušais')
else:
    print('seniors')