''' 
You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1

Solution - greedy
while standing at one index we check what is the end of our current jump and we also check the farthest we can reach from the range of next indexes in our current jump. 
we increment step when we reach end i.e. end of our current jump and we must take a jump
'''

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        steps = 0
        end = 0
        farthest = 0
        
        # We stop at n-2 because once we reach the last index, no more jumps are needed
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            
            if i == end:  # time to make a jump
                steps += 1
                end = farthest
                
        return steps
