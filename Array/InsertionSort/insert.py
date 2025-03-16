def insert(list_a):
    print(f"Original list: {list_a}\n")
    indexing_length = range(1, len(list_a))

    for i in indexing_length:
        valuetosort = list_a[i]
        print(f"Starting iteration {i}: trying to place {valuetosort} correctly")

        while i > 0 and list_a[i - 1] > valuetosort:
            print(f"  {list_a[i - 1]} (at index {i-1}) is greater than {valuetosort}, swapping...")

            # Swap the elements
            list_a[i], list_a[i - 1] = list_a[i - 1], list_a[i]
            i = i - 1  # Move the index back to compare again

            print(f"  List after swap: {list_a}")

        print(f"Placed the value to sort {valuetosort} at the correct position: {list_a}\n")

    print(f"Sorted list: {list_a}")
    return list_a

# Example usage:
insert([5, 3, 8, 4, 2])
