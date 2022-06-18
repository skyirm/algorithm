def insert_sort(alist):
    for i in range(1, len(alist)):
        current_value = alist[i]
        index = i

        while index > 0 and alist[index-1] > current_value:
            alist[index] = alist[index-1]
            index = index-1

        alist[index] = current_value


if __name__ == "__main__":
    a = [13, 421, 41, 51, 51, 345, 636, 2, 6, 36, 0]
    insert_sort(a)
    print(a)
