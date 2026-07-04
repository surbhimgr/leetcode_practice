''' Q1. Unique Middle Element
Solved
Easy
3 pt.
You are given an integer array nums of odd length n.

Return true if the middle element of nums appears exactly once in the array. Otherwise return false.
'''

class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        m=nums[len(nums)//2]
        return nums.count(m)==1©leetcode
