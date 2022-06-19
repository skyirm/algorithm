def quick_sort(alist):
    quick_sort_helper(alist, 0, len(alist)-1)


def quick_sort_helper(alist, first, last):
    if first < last:
        splitposition = partition(alist, first, last)

        quick_sort_helper(alist, first, splitposition-1)
        quick_sort_helper(alist, splitposition+1, last)


def partition(alist, first, last):
    pivotvalue = alist[first]

    left_mark = first+1
    right_mark = last
    done = False

    while not done:
        while left_mark <= right_mark and alist[left_mark] <= pivotvalue:
            
            left_mark += 1
        while alist[right_mark] >= pivotvalue and left_mark <= right_mark:
            right_mark -= 1
        if left_mark > right_mark:
            done = True
        else:
            temp = alist[right_mark]
            alist[right_mark] = alist[left_mark]
            alist[left_mark] = temp

    temp = alist[right_mark]
    alist[right_mark] = alist[first]
    alist[first] = temp
    return right_mark


if __name__ == "__main__":
    a = [13, 421, 41, 51, 51, 345, 636, 2, 6, 36, 0]
    quick_sort(a)
    print(a)
