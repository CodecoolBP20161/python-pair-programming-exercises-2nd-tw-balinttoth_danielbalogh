import string
import random

def generate_password():

    char_list = []

    low_abc = string.ascii_lowercase
    cap_abc = string.ascii_uppercase
    numbers = list(range(0, 10))

    length = random.randint(8, 16)

    for char in range(1, length):
        which_char_type = random.randint(1, 4)
        if which_char_type == 1:
            list_to_choose_from = low_abc
        elif which_char_type == 2:
            list_to_choose_from = cap_abc
        else:
            list_to_choose_from = numbers
        chosen_char = str(list_to_choose_from[random.randint(0, len(list_to_choose_from)-1)])
        char_list.append(chosen_char)

    password = "".join(char_list)

    return password


def main():

    print(generate_password())


main()
