# Replaced the implementation from the LMS because it was based on creation of
# temp lists and it wasn't effective, it has shown worse performance that
# `insertion` in all cases.
# In-place merge sort using slice assignment.
def merge_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr)

    if high - low <= 1:
        return arr

    mid = (low + high) // 2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid, high)
    merge(arr, low, mid, high)

    return arr


def merge(arr, low, mid, high):
    left = arr[low:mid]
    right = arr[mid:high]

    left_index = 0
    right_index = 0
    write_index = low

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            arr[write_index] = left[left_index]
            left_index += 1
        else:
            arr[write_index] = right[right_index]
            right_index += 1
        write_index += 1

    remaining_left = len(left) - left_index
    arr[write_index:write_index + remaining_left] = left[left_index:]
    write_index += remaining_left
    remaining_right = len(right) - right_index
    arr[write_index:write_index + remaining_right] = right[right_index:]
