number = int(input("Enter a number: "))

for number in range(1, number+1):
    if number % 3 == 0 and number % 5 == 0:
        message = "fizzbuzz"
    elif number % 3 == 0:
        message = "fizz"
    elif number % 5 == 0:
        message = "buzz"
    else:
        message = number
    print(message)


