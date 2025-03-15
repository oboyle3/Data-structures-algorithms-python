

def the_bub(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:  # Compare with the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap if out of order
    return arr



arr = [10, 13, 9, 14, 1]
print(f"sorted :")
#the_bub(arr)
print(the_bub(arr))