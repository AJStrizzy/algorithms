def quick_sort(sequence):
    length = len(sequence)

    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater) 

print(quick_sort([6,4,7,9,2,3,4,6,7,8,9]))                           