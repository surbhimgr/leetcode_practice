'''
Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i, j < nums.length
i != j
|nums[i] - nums[j]| == k
Notice that |val| denotes the absolute value of val. 

solution - maintain a seen set and pairs set, add items to seen after visiting them, add items to pairs if k+current items exists in seen
'''

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0

        seen, pairs = set(), set()
        for num in nums:
            if num - k in seen:
                pairs.add((num - k, num))
            if num + k in seen:
                pairs.add((num, num + k))
            seen.add(num)
        return len(pairs)


        
