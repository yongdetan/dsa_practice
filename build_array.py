nums = [5,0,1,2,3,4]

def build_array(nums):
    return [nums[nums[i]] for i in range(len(nums))]
print(build_array(nums))