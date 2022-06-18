def merge_sort(alist):
    if len(alist) > 1:
        mid_point = len(alist)//2
        left_half = alist[:mid_point]
        right_half = alist[mid_point:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                alist[k] = left_half[i]
                i += 1
            else:
                alist[k] = right_half[j]
                j += 1
            k += 1
        while i<len(left_half):
            alist[k]=left_half[i]
            i+=1
            k+=1
        while j<len(right_half):
            alist[k]=right_half[j]
            j+=1
            k+=1

if __name__ == "__main__":
    a = [13, 421, 41, 51, 51, 345, 636, 2, 6, 36, 0]
    merge_sort(a)
    print(a)