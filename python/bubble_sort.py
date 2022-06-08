sequence = [4, 3, 5, 0, 1]


# swaps = 0


# Your Code Here

def bubble(list_a):
    indexing_length = len(list_a) - 1
    _sorted = False
    swaps = 0
    while not _sorted:
        _sorted = True

        for i in range(0, indexing_length):
            if list_a[i] > list_a[i + 1]:
                _sorted = False
                list_a[i], list_a[i + 1] = list_a[i + 1], list_a[i]
                swaps += 1
    return list_a, swaps


print(bubble([4, 8, 1, 14, 8, 2, 9, 5, 7, 6, 6]))
print(bubble(sequence))
# print(f"Final result: {sequence}")
# print(f"Swaps: {swaps}")
