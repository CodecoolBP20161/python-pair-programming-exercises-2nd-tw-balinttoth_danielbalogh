def fizzbuzz():

    list_1_100 = []

    for i in range(0, 101):
        list_1_100.append(i)

    for number in range(1, 101):
        if int(number) % 15 == 0:
            list_1_100[number] = ("FizzBuzz")
        elif int(number) % 3 == 0:
            list_1_100[number] = ("Fizz")
        elif int(number) % 5 == 0:
            list_1_100[number] = ("Buzz")

    for number in list_1_100[1:]:
        print(number)



def main():

    fizzbuzz()




if __name__ == '__main__':
    main()
