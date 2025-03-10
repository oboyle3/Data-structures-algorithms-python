'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''
target = 5
sample_arr = [10,2,3,17]

def twoSum(arr,target):
    counter = target
    n = len(arr)
    for i in range(n):
        for j in range(i + 1,n):
            if arr[i] + arr[j] == counter:
                print(f"we found two indices that add to the target {arr[i]} and {arr[j]}")
                return i,j

result = twoSum(sample_arr,target)
print(f"result {result}")
                




