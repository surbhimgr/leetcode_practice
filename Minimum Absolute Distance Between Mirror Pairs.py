''' Minimum Absolute Distance Between Mirror Pairs
You are given an integer array nums.

A mirror pair is a pair of indices (i, j) such that:

0 <= i < j < nums.length, and
reverse(nums[i]) == nums[j], where reverse(x) denotes the integer formed by reversing the digits of x. Leading zeros are omitted after reversing, for example reverse(120) = 21.
Return the minimum absolute distance between the indices of any mirror pair. The absolute distance between indices i and j is abs(i - j).

If no mirror pair exists, return -1. '''

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        dic={}
        INF=10**18
        mindif = INF
        rev = int(str(nums[0])[::-1])
        dic[rev]=0
        for i in range(1,len(nums)):
            rev = int(str(nums[i])[::-1])
            if nums[i] in dic:
                mindif=min(i-dic[nums[i]],mindif)
            dic[rev] = i
        if mindif == INF:
            mindif = -1
        return mindif
        
