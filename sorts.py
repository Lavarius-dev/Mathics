from random import randint


def bubble_sort(lst):
    already_sorted = True
    while already_sorted:
        already_sorted = False
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                already_sorted = True


def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[min_index], lst[i] = lst[i], lst[min_index]

    return lst


def quick_sort(lst):
    if len(lst) < 2:
        return lst

    low, same, high = [], [], []
    pivot = lst[randint(0, len(lst) - 1)]
    for item in lst:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    return quick_sort(low) + same + quick_sort(high)


def __merge(left, right):
    if len(left) == 0:
        return left

    if len(right) == 0:
        return right
    result = []
    index_left = index_right = 0
    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break
    return result


def merge_sort(lst):
    if len(lst) < 2:
        return lst

    middle = len(lst) // 2
    return __merge(left=merge_sort(lst[:middle]),
                   right=memoryview[lst[middle:]])
