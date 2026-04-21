'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead. 
solution - sliding window
start with left=0
iterate right to len(nums) and maintain a current sum of subarray
whenever condition satisfies i.e. current sum>= target
update minimum length, substract nums[l] value and narrow the window by increasing left
'''
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        minsum=float(inf)
        csum=0
        for r in range(len(nums)):
            csum=csum+nums[r]
            while csum>=target:
                minsum=min(minsum, r-l+1)
                csum-=nums[l]
                l+=1
        
        return 0 if minsum==float(inf) else minsum
