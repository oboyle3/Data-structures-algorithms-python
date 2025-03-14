def insert(arr):
    indexingLength = range(1, len(arr))
    print(f"Original array: {arr}\n")

    for i in indexingLength:
        value_to_sort = arr[i]
        print(f"Pass {i}: Trying to place {value_to_sort} in the correct position")

        while i > 0 and arr[i - 1] > value_to_sort:
            print(f"  {arr[i-1]} is greater than {value_to_sort}, swapping...")
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
            print(f"  New array state: {arr}")

        print(f"  {value_to_sort} placed at index {i}")
        print(f"  Array after pass {i}: {arr}\n")

    print("Sorted array:", arr)
    return arr

# Example Usage
arr = [64, 34, 25, 12, 22, 11, 90]
insert(arr)
