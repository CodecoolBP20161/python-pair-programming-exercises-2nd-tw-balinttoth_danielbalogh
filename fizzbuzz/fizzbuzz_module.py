def fizzbuzz(number):
    if (float(number) / 15) == round(number / 15) :
        print("Fizzbuzz")
    elif (float(number) / 3) == round(number / 3) :
        print("Fizz ")
    elif (float(number) / 5) == round(number / 5) :
        print("Buzz")
    else :
        print number
    return


def main():
    for x in range(1, 101):
        fizzbuzz(x)
    return

if __name__ == '__main__':
    main()
