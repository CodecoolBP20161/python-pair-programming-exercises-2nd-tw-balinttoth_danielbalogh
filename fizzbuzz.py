def fizzbuzz(number):

    if number % 15 == 0:
        number = "Fizzbuzz"
    elif number % 5 == 0:
        number = "Buzz"
    elif number % 3 == 0:
        number = "Fizz"
    else:
        number = number

    return number


def main():

    for number in range(1, 101):

            print(fizzbuzz(number))

main()
