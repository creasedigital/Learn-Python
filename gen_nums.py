def gen_nums():
    max_num = 100
    nums = (1, 2, 3, 4)
    i = 0
    results = []
    while len(results) < max_num:
        if i >= len(nums): i = 0
        results.append(nums[i])
        i += 1
    return results
    
print(gen_nums())