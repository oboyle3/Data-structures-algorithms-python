

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Example usage:
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Sorted array:", arr)

def insert(list_a):
    indexing_length = range(1, len(list_a))
    for i in indexing_length:
        valuetosort = list_a[i]

        while list_a[i -1] > valuetosort and i>0:
            list_a[i], list_a[-1] = list_a[-1], list_a[i]
            i =i -1 #look at next item
    return list_a

arr2 = [12, 11, 13, 5, 6]
insert(arr2)
print("Sorted array:", arr2)