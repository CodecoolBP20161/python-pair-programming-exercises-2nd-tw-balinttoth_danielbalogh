a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def listoverlap(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    sets = (set1 & set2)
    lists = list(sets)
    print (lists)

    return


def main():
    listoverlap(a, b)
    return 


if __name__ == '__main__':
    main()
