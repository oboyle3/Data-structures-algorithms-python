#given a array of numbers find the number that is higest in that array and print it
'''
psudo code
for loop array

'''
def find_max(arr):
    #initailize the first element in the array as max
    max_num = arr[0]
    print(f"initial max num: {max_num}")
    #loop through array
    for num in arr:
        print(f"checking number:  {num}") #print the current number being checked
        if num > max_num:
            print(f"we found a new max: {num} > {max_num}")
            max_num = num
            print(num)
    return max_num #retrun max num

#test function
numbers = [12,3,2,7,17,8,4]

print(find_max(numbers))