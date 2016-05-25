import datetime


def years(age):
    x = datetime.datetime.now()
    this_year = x.year
    one_hunder_years_old = int(this_year) - int(age) + 100
    return one_hunder_years_old


def main():
    name = input("What is your name?: ")
    age = (input("How old are you?: "))
    years(age)
    print("Dear %s, I would like to inform you, that you will turn 100 in %s." % (name, years(age)))
    return


if __name__ == '__main__':
    main()
