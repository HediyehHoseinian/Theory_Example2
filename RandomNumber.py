import random

numbers = []
i = 0

while True:
    Number = input("enter length: ")
    if Number.isdigit() and int(Number) > 0:
        n = int(Number)
        break
    else:
        print("you didn't enter valid number")


while i < n:
    x = random.choice(range(1000))
    if x not in numbers:
        numbers.append(x)
        i += 1