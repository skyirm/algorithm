def shellsort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for start_point in range(sublistcount):
            gap_insertion_sort(alist, start_point, sublistcount)
        sublistcount = sublistcount//2


def gap_insertion_sort(alist, start, gap):
    for i in range(start, len(alist), gap):

        current_value = alist[i]
        position = i
        while position >= start and alist[position-gap] > current_value and position-gap > start:
            alist[position] = alist[position-gap]
            position = position-gap

        alist[position] = current_value


if __name__ == "__main__":
    a = [13, 421, 41,67]
    shellsort(a)
    print(a)
