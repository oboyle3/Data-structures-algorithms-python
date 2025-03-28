my_list = [1,2,3,4,5]
my_str_list = ["apple", "banana", "cherry"]

print(my_list)
#print(my_list[0])
my_list.append(6)
#print(my_list)
def function(arr):
    n = len(my_list)
    for i in range(n):
        if arr[i] == 3:
            print(f"hello world")
    

print(f"the result {function(my_list)}")
