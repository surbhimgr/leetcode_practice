''' Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Approach - fix one no. and solve remaining array as 2 sum
O(n^2)
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans=float('inf')
        for k in range(n-2):
            i, j = k+1, n-1
            while i < j:
                total = nums[i]+nums[k]+nums[j]
                if abs(target-total)<abs(target-ans):
                    ans=total
                if total<target:
                    i += 1
                elif total>target:
                    j -= 1
                else:
                    return total

        return ans
