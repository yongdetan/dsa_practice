nums = [3,2,4]
target = 6

def twoSum(nums, target):
    dict = {}
    for i, v in enumerate(nums):
        remaining = target - v
        if remaining in dict:
            return [dict[remaining], i]
        dict[v] = i


print(twoSum(nums,target))

