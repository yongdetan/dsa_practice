nums = [1,3,5,6]
target = 3

def searchInsert(nums, target):
    if target in nums:
        return nums.index(target)
    else:
        low = 0
        high = len(nums) - 1
        for x in nums:
            mid = (high + low) // 2
            if nums[mid] > target:
                high = mid - 1
            if nums[mid] < target:
                low = mid + 1
        return low

print(searchInsert(nums, target))