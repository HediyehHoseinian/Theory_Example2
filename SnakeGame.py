InputNumber = int(input("Enter a Number = "))

for i in range(InputNumber):

    if i % 2 == 0:

        print("=", end="")

    else:
        print("(",end=")")