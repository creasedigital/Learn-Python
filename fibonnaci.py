def fib(arr):
    sum = 0
    curr_arr = []
    i = 0
    
    while i < len(arr):
        sum += arr[i]
        curr_arr.append(sum)
        i += 1
    
    return curr_arr
    
print(fib([1,2,3,4,5]))