number = int(input("Enter a number: "))

for number in range(1, number+1):
    if number % 3 == 0 and number % 5 == 0:
        x = "fizzbuzz"
    elif number % 3 == 0:
        x = "fizz"
    elif number % 5 == 0:
        x = "buzz"
    else:
        x = number
    print(x)


