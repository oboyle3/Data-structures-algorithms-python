arry = [5, 3, 8, 4, 2]

def bubble_sort(arr):
    # Get the length of the array
    n = len(arr)
    
    # Outer loop to iterate through the entire array
    for i in range(n):
        # Flag to check if any swapping happened in this pass
        swapped = False
        
        # Inner loop to compare adjacent elements
        for j in range(0, n - i - 1):
            # Compare the current element with the next element
            if arr[j] > arr[j + 1]:
                # If the current element is greater, swap them
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # Mark that a swap happened
        
        # If no elements were swapped in the inner loop, the array is already sorted
        if not swapped:
            break  # Exit the loop early since the list is sorted

    # Return the sorted array
    return arr

# Example Usage
arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array:", bubble_sort(arr))


print("Sorted array:", bubble_sort(arry))