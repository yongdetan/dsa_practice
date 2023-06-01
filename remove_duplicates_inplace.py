nums = [0,0,1,1,1,2,2,3,3,4]

def removeDuplicates(nums):
    uniqueCheck = {}
    k = len(nums)
    i = 0
    while i < k:
        if nums[i] in uniqueCheck:
            k -= 1
            del nums[i]     
        else:      
            uniqueCheck[nums[i]] = 1
            i += 1
    return len(nums)

print(removeDuplicates(nums))