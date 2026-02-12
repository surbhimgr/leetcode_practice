''' Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them. '''

from itertools import product
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = [''] * len(nums)
        for i in range(len(nums)):
            c = nums[i][i]
            res[i] = '1' if c == '0' else '0'
        return ''.join(res)


        
