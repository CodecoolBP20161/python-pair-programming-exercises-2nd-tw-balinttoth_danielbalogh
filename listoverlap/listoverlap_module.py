a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def listoverlap(list1, list2):

    sets = (set(list1) | set(list2))
    # sets = (set(list1) & set(list2)) - That is what the readme says...
    return sorted(list(sets))


def main():
    print(listoverlap(a, b))
    return


if __name__ == '__main__':
    main()
