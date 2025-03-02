
def min_num(arr):
    #assign the counter to the first element in array
    current_min_value = arr[0]
    #loop through array
    for num_being_checked in arr:
        print(f"current min value: {current_min_value}")
        print(f"number currently being checked: {num_being_checked}")
        if num_being_checked < current_min_value:
            current_min_value = num_being_checked
            print(current_min_value)
        else:
            print(f"else because {num_being_checked} is less than {current_min_value}")

    return current_min_value


numbers = [23,21,13,11,8,1]
print(min_num(numbers))