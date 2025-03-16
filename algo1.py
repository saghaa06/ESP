def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    A = merge_sort(left_half)
    B = merge_sort(right_half)
    return merge(A, B)


def merge(A, B):
    sorted_list = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            sorted_list.append(A[i])
            i += 1
        else:
            sorted_list.append(B[j])
            j += 1
    sorted_list.extend(A[i:])
    sorted_list.extend(B[j:])
    return sorted_list
