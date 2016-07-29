a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def merge(list1, list2):

    list1_2 = list(set(list1) & set(list2))
    return list1_2


def main():

    print(merge(a, b))


main()
