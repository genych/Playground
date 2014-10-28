def merge_sort(lst, c=0):
    """ 
    Merge sort with counter of inversions
    """

    if len(lst) == 1: return 0
    m = len(lst) / 2
    left = lst[:m]
    right = lst[m:]

    l = merge_sort(left, c)
    r = merge_sort(right, c)

    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[j]
            j += 1
            c += len(left) - i
        k += 1
    if i == len(left):
        lst[k:] = right[j:]
    else:
        lst[k:] = left[i:]

    return c + l + r
