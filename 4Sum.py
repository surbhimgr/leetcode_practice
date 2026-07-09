''' 
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order. 

Solution :
sort array, fix 2 nos. and apply two pointers to find remaining 2 nos.
time complexity - O(n^3)
'''

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        ans=[]
        for n1 in range(n-3):
            if n1>0 and nums[n1]==nums[n1-1]:
                continue
            for n2 in range(n1+1,n-2):
                if n2>n1+1 and nums[n2]==nums[n2-1]:
                    continue
                n3=n2+1
                n4=n-1
                while n3<n4:
                    tot=nums[n1]+nums[n2]+nums[n3]+nums[n4]
                    if tot==target:
                        a1=[nums[n1],nums[n2],nums[n3],nums[n4]]
                        ans.append([nums[n1],nums[n2],nums[n3],nums[n4]])
                        n3+=1
                        n4-=1
                        while n3 < n4 and nums[n3] == nums[n3 - 1]:
                            n3 += 1
                        while n3 < n4 and nums[n4] == nums[n4 + 1]:
                            n4 -= 1
                    elif tot<target:
                        n3+=1
                    else:
                        n4-=1
        return ans
