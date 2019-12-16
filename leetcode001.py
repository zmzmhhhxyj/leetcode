def twoSum(nums, target):
    d = {}
    for i, n in enumerate(nums):
        m = target - n
        if m in d:
            return [d[m], i]
        else:
            d[n] = i

a=twoSum([2, 11, 15, 7],9)
print(a)