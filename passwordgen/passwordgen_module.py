import string
import random

def passwordgen():
    char_list = []

    low_abc = list(string.ascii_lowercase)
    cap_abc = list(string.ascii_uppercase)
    numbers = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    symbols = ('@', '!', '?', ':', '+', '-' '#', '$', '%', '^', '&', '*', '(', ')', '?')

    length = random.randint(8,15)

    for char_num in range(1, length+1) :
        which_list = random.randint(1, 4)
        if which_list == 1 :
            list_used = low_abc
        if which_list == 2 :
            list_used = cap_abc
        if which_list == 3 :
            list_used = numbers
        if which_list == 4 :
            list_used = symbols
        added_char = list_used[random.randint(0, list_used.index(list_used[-1]))]
        char_list.append(added_char)
    password = "".join(char_list)

    return password


def main():
    print(passwordgen())
    return


if __name__ == '__main__':
    main()
