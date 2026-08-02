'''
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears at most twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3] 

Solution- sort it and check if next element is same, maintain a prev variable for avoiding duplicates
'''

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans=[]
        prev=0
        for i in range(len(nums)-1):
            if prev==0:
                if nums[i]==nums[i+1]:
                    ans.append(nums[i])
                    prev=1
            else:
                prev=0
                continue
        return ans
        
