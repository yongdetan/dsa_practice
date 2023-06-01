nums1 = [2,3,7,0,0,0]
nums2 = [1,5,6]

def merge(nums1, m, nums2, n):  
    nums1[m:] = nums2[:n] #replace the  elements (all the 0s) that need to be merged with nums2 elements (until n)
    nums1.sort()

def merge2(nums1, m, nums2, n):
    while n: #there will always be n amount of spaces empty within nums1 for nums2 elements to merge
        
        if m and nums1[m - 1] >= nums2[n - 1]: #if m prevents the list from going out of range (happens if the first element of nums2 is the same or smaller than the first element of nums1)
            print(m,n,nums1[m-1], nums2[n-1], nums1, "a")
            nums1[m + n - 1] = nums1[m - 1] 
            m -= 1 
        
        else:
            print(m,n,nums1[m-1], nums2[n-1], nums1, "b")
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1

def merge3(nums1, m, nums2, n):
    pos = m+n-1
    i = m-1
    j = n-1

    while(i>=0 or j>=0):
        if(i>=0 and j>=0):
            if(nums1[i]>=nums2[j]):
                nums1[pos] = nums1[i]
                i -= 1
            else:
                nums1[pos] = nums2[j]
                j -= 1
        if(j>=0):
            nums1[pos] = nums2[j]
            j -= 1
        else:
            break

        pos-=1


merge2(nums1, 3, nums2, 3)
print(nums1)